# user/api_urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .api_views import LoginAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="api-login"),
    path("refresh/", TokenRefreshView.as_view(), name="api-refresh"),
]
