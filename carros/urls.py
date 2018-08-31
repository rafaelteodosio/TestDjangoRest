from django.conf.urls import url, include
from rest_framework import routers
from carros import views

router = routers.DefaultRouter()
router.register(r'car', views.CarViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
