from django.contrib.auth import get_user_model
from rest_framework import permissions

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from .serializers import UserSerializer


class SignUpView(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class SignInView(TokenObtainPairView):
    permission_classes = [AllowAny]


class RefreshView(TokenRefreshView):
    permission_classes = [TokenRefreshView]
