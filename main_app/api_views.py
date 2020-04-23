from rest_framework import generics
from main_app.models import *
from main_app.serializers import *


class GenreListApiView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
