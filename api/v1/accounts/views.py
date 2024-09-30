from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from accounts.models import User
from api.v1.accounts.serializers import UserSerializer, RegisterSerializer, LoginSerializer


class RegisterView(generics.CreateAPIView):
    """Register a new user.

    """
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


class UserListAPIView(generics.ListAPIView):
    """
    List all users. Available only for admins.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class LoginView(generics.GenericAPIView):
    """Login the user and return an access token

    """
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)
