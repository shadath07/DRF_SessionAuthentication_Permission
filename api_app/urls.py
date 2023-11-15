from django.urls import path,include
from . import views 
from rest_framework.routers import DefaultRouter


# creating Router object
router = DefaultRouter()
router.register('studentapi', views.StudentModelViewSet,basename= 'student')

urlpatterns= [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='rest_framework')),
]

