from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard')
]