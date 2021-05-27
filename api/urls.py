""" api app urls configuration """
from django.urls import include, path
from rest_framework import routers
from . import views


# API routes
router = routers.DefaultRouter()
router.register(r'contacts', views.ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
