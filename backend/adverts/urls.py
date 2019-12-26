from django.conf.urls import url, include
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register('adverts', views.AdvertView, basename='Adverts')
routers.register('orgs', views.OrgView)

urlpatterns = [
    url(r'', include(routers.urls))
]