from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r"cars", views.CarViewSet)
router.register(r"rate", views.RateViewSet)
router.register(r"popular", views.PopularViewSet)

urlpatterns = [url(r"^", include(router.urls))]
