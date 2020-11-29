from rest_framework.permissions import AllowAny
from api.models import Star
from django.contrib.auth.models import User
from api.serializers import StarSerializer
from api.serializers import StarDetailedSerializer
from api.serializers import UserSerializer
from rest_framework import generics
from rest_framework import permissions


class StarsView(generics.ListAPIView):
    queryset = Star.objects.all()
    serializer_class = StarSerializer


class StarsDetailedView(generics.ListCreateAPIView):
    queryset = Star.objects.all()
    serializer_class = StarDetailedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StarView(generics.RetrieveAPIView):
    queryset = Star.objects.all()
    serializer_class = StarSerializer


class StarDetailedView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Star.objects.all()
    serializer_class = StarDetailedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
