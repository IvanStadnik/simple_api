from django.urls import path

from api.v1.accounts import views


urlpatterns = [
    path('', views.UserListAPIView.as_view(), name='user-list'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
]