from django.contrib import admin
from django.conf.urls import url, include
from . import views
from tigtag.views import CustomerViewSet,WaitingListViewSet
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register(r'customers', views.CustomerViewSet, basename='customer')
router.register(r'waiting', views.WaitingListViewSet, basename='waiting')
 

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^index.html', views.request_index, name="home"), 
    url(r'^waiting_list.html', views.request_waiting_list, name="home"), 

]

