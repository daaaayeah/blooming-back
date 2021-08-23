from django.urls import path

from .views import RefreshView, SignInView, SignUpView


urlpatterns = [
    path('signin/', SignInView.as_view()),
    path('refresh/', RefreshView.as_view()),
    path('signup/', SignUpView.as_view())
]
