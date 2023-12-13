from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from .serializers import sirializers

class UserViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated,)
    serializer_class = sirializers
    queryset = get_user_model().objects.all()