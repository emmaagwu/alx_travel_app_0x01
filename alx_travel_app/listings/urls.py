from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r"listings", ListingViewSet, basename="listing")
router.register(r"bookings", BookingViewSet, basename="booking")

urlpatterns = [
    path("api/", include(router.urls)),
]