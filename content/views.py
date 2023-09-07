from django.shortcuts import render
from rest_framework.views import APIView
from .models import Post


class Main(APIView):
    def get(self, request):
        posts = Post.objects.all()

        print(posts)

        return render(
            request,
            "twitter/main.html",
            {"posts": posts},
        )
