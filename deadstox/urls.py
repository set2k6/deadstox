
from django.conf.urls import url, include
from rest_framework import routers
from deadstox import views


router = routers.DefaultRouter()
router.register(r'closets', views.ClosetsViewSet)
router.register(r'sneakers', views.SneakersViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
# from django.conf.urls import url

# from . import views

# urlpatterns = [
    # url(r'^$', views.index, name='index'),

    # url(r'^register/', views.Register.as_view(), name='register'),

    # url(r'^login_user/', views.login_user, name='login_user'),

    # url(r'^login/', views.Login.as_view(), name='login'),

    # url(r'^login/', views.logout_user, name='logout'),

    # url(r'^register_user/', views.register_user, name='register_user'),

#     url(r'^closets/$', views.closetCreate, name='closets_add'),

#     url(r'^sneakers/$', views.sneakerCreate, name='sneaker_add'),

#     url(r'^datetimecurrent/$', views.current_datetime, name='datetimecurrent'),

# ]
