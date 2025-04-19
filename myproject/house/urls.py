from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='user-list')
router.register(r'property', PropertyViewSet, basename='property-list')
router.register(r'review', ReviewViewSet, basename='review-list')
router.register(r'region', RegionViewSet, basename='region-list')
router.register(r'city', CityViewSet, basename='city-list')
router.register(r'district', DistrictViewSet, basename='district-list')



urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]


