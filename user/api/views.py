from rest_framework import viewsets, permissions
from .serializers import GroupSerializer, UserSerializer
from ..models import Group, User

from rest_framework.response import Response


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
