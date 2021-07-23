from django.urls import path, include
from project.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from rest_framework_nested import routers

client = routers.DefaultRouter()
client.register(r'clients', ClientViewSet, basename="Project")

urlpatterns = [
    path('', include(client.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]