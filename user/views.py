from django.shortcuts import render
from rest_framework.views import APIView
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from .models import Follow
from rest_framework import status


class Login(APIView):
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        print(email, password)
        if email is None:
            return Response(status=500, data=dict(message="이메일을 입력해주세요"))

        if password is None:
            return Response(status=500, data=dict(message="비밀번호를 입력해주세요"))

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(status=500, data=dict(message="입력정보가 잘못되었습니다."))

        if check_password(password, user.password) is False:
            return Response(status=500, data=dict(message="입력정보가 잘못되었습니다."))

        request.session["loginCheck"] = True
        request.session["email"] = user.email

        return Response(status=200, data=dict(message="로그인에 성공했습니다."))


class Join(APIView):
    def get(self, request):
        return render(request, "user/join.html")

    def post(self, request):
        password = request.data.get("password")
        email = request.data.get("email")
        user_id = request.data.get("user_id")
        name = request.data.get("name")

        if User.objects.filter(email=email).exists():
            return Response(status=500, data=dict(message="해당 이메일 주소가 존재합니다."))
        elif User.objects.filter(user_id=user_id).exists():
            return Response(
                status=500, data=dict(message='사용자 이름 "' + user_id + '"이(가) 존재합니다.')
            )

        # make_password(password)
        User.objects.create(
            password=make_password(password), email=email, user_id=user_id, name=name
        )

        return Response(status=200, data=dict(message="회원가입 성공했습니다. 로그인 해주세요."))


class LogOut(APIView):
    def get(self, request):
        request.session.flush()
        return render(request, "user/login.html")


class FollowAPIView(APIView):
    def post(self, request):
        user = request.user  # 현재 로그인한 사용자
        following_email = request.data.get("following_email")  # 팔로우할 사용자의 이메일

        if user and following_email:
            # 팔로우 관계 생성 또는 이미 팔로우 중인 경우 제거
            try:
                follow = Follow.objects.get(
                    follower=user.email, following=following_email
                )
                follow.delete()
                return Response({"message": "팔로우를 취소했습니다."}, status=status.HTTP_200_OK)
            except Follow.DoesNotExist:
                Follow.objects.create(
                    follower=user.email, following=following_email, is_live=True
                )
                return Response(
                    {"message": "팔로우 되었습니다."}, status=status.HTTP_201_CREATED
                )
        else:
            return Response(
                {"message": "로그인 후 사용 가능한 기능입니다."}, status=status.HTTP_401_UNAUTHORIZED
            )
