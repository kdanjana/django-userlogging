from django.urls import path
from . import views


app_name = "mainapp"

urlpatterns =[
    path("", views.main_page, name="main"),
    path("signup/", views.SignupPage.as_view(), name="signup"),
    path("login/", views.LoginPage.as_view(), name="login"),
    path("logout/", views.LogoutPage, name="logout"),
    path("sp_success/", views.signup_success, name="signup_success"),
    path("ln_success/", views.login_success, name="login_success")
]