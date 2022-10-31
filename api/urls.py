from django.urls import path

from .views import LoginView, UserRegistrationView, ImageVerificationView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path('upload/', ImageVerificationView.as_view(), name='file-upload'),
]
