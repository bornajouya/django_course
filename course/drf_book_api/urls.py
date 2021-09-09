from django.urls import path
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from . import views
from .views import UserViewSet,CommnetViewSet,SaveUesrViewSet
from .views import LoginView
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'commnets', CommnetViewSet)
router.register(r'save_uesr', SaveUesrViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view()),

]