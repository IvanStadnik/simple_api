from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions, mixins, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.response import Response

from accounts.models import User
from api.v1.accounts.serializers import UserSerializer, RegisterSerializer, LoginSerializer
from api.v1.manuscripts.serializers import ManuscriptCreateSerializer, ManuscriptListSerializer, CategorySerializer
from manuscripts.models import Manuscript, ManuscriptCategory


class ManuscriptsListCreateView(generics.ListCreateAPIView):
    """Register a new user.

    """
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ManuscriptListSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        """Admin can see all manuscripts and regular users only their own manuscripts.

        :return:
        """
        queryset = Manuscript.objects.all()
        user = self.request.user
        if not user.is_authenticated:
            return Manuscript.objects.none()
        elif not user.is_staff:
            return queryset.filter(created_by=user)

        return queryset

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ManuscriptCreateSerializer
        return super(ManuscriptsListCreateView, self).get_serializer_class()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)


class ManuscriptsCategoryCreateApiView(generics.CreateAPIView):
    """Only admins can create categories

    """
    serializer_class = CategorySerializer
    queryset = ManuscriptCategory.objects.all()
    permission_classes = [permissions.IsAdminUser]


class ManuscriptsCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = ManuscriptCategory.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
