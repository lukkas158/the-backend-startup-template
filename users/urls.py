from django.urls import path
from users.views import UserViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()

router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name="token"),
    path('token/refresh/',  TokenRefreshView.as_view(), name="refresh-token")
]


urlpatterns += router.urls
