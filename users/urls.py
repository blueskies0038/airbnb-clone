from django.urls import path
from . import views


app_name = "users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("login/github/", views.github_login, name="github_login"),
    path("login/github/callback", views.github_callback, name="github_callback"),
    path("logout/", views.LogOut, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("verify/<str:key>", views.complete_verify, name="verify"),
    path("<int:pk>/", views.UserProfileView.as_view(), name="profile"),
]