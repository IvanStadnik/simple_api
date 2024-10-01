from django.urls import path, include

urlpatterns = [
    path('users/', include('api.v1.accounts.urls')),
    path('manuscripts/', include('api.v1.manuscripts.urls'))
]