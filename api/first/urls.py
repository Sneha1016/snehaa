from django.urls import path
from .views import UserViewSet

urlpatterns = [
    path ('login',UserViewSet.as_view(),name='login'),
]
