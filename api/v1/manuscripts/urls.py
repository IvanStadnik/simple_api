from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.v1.manuscripts import views


router = DefaultRouter()
router.register(r'categories', views.ManuscriptsCategoryViewSet, basename='category')

urlpatterns = [
    path('', views.ManuscriptsListCreateView.as_view(), name='manuscripts-list-create'),
    path('', include(router.urls)),
]