from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from datetime import datetime


class Main(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by("-created_at")
        user_email = request.session.get("email", None)

        print(posts)

        return render(
            request,
            "twitter/main.html",
            {"posts": posts, "user_email": user_email},
        )


class UploadFeed(APIView):
    def post(self, request):
        content = request.data.get("content")
        user_id = request.data.get("user_id")
        created_at = datetime.now()  # 현재 시간 가져오기

        Post.objects.create(  # 데이터베이스에 데이터 생성
            content=content, user_id=user_id, like_count=0, created_at=created_at
        )

        return Response(status=200)


class DeletePost(APIView):
    url = "/delete-post/"

    def post(self, request):
        post_id = request.data.get("post_id")  # post_id로 수정
        user_email = request.session.get("email", None)

        try:
            post = Post.objects.get(id=post_id)  # id로 포스트를 찾음

            # 글의 작성자와 로그인한 사용자를 비교하여 삭제 여부 확인
            if post.user_id == user_email:
                post.delete()
                return Response({"message": "글이 삭제되었습니다."}, status=200)
            else:
                return Response({"message": "글을 삭제할 수 있는 권한이 없습니다."}, status=403)
        except Post.DoesNotExist:
            return Response({"message": "삭제할 글을 찾을 수 없습니다."}, status=404)
