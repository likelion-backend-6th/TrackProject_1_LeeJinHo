from django.urls import path
from .views import Login, Join, LogOut, FollowAPIView

urlpatterns = [
    path("login", Login.as_view(), name="login"),
    path("logout", LogOut.as_view(), name="logout"),
    path("join", Join.as_view(), name="join"),
    path("follow/", FollowAPIView.as_view(), name="follow"),
]
