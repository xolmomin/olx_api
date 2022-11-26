from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import UserModelViewSet, RegionModelViewSet, AdvertModelViewSet, DistrictModelViewSet, \
    ComplainModelViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('users', UserModelViewSet, basename='users')
router.register('adverts', AdvertModelViewSet, basename='adverts')
router.register('regions', RegionModelViewSet, basename='regions')
router.register('districts', DistrictModelViewSet, basename='districts')
router.register('complains', ComplainModelViewSet, basename='complains')

urlpatterns = [
    # path('token', views.obtain_auth_token),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
