from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from datetime import datetime


class Main(APIView):
    def get(self, request):
        posts = Post.objects.all()

        print(posts)

        return render(
            request,
            "twitter/main.html",
            {"posts": posts},
        )


class UploadFeed(APIView):
    def post(self, request):
        content = request.data.get("content")
        user_id = request.data.get("user_id")
        created_at = datetime.now()  # 현재 시간 가져오기
        print(content)
        print(user_id)

        Post.objects.create(  # 데이터베이스에 데이터 생성
            content=content, user_id=user_id, like_count=0, created_at=created_at
        )

        return Response(status=200)
