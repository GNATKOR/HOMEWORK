from .views import UsersView, SignupView, SignInView
from django.urls import path

urlpatterns = [
    path('', UsersView.as_view()),
    path('sign-up/', SignupView.as_view()),
    path('sign-in/', SignInView.as_view())
]
