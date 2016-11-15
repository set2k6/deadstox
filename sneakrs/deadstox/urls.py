
from django.conf.urls import url, include
from rest_framework import routers
from deadstox import views


router = routers.DefaultRouter()
router.register(r'closets', views.ClosetsViewSet)
router.register(r'sneakers', views.SneakersViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

]

