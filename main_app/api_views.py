from rest_framework import generics, viewsets, permissions, filters
from rest_framework.mixins import CreateModelMixin

from main_app.models import *
from main_app.serializers import *


# GENRE:

class GenreListApiView(generics.ListCreateAPIView):
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]

    def get_queryset(self):
        user = self.request.user
        return Genre.objects.filter(user=user).order_by("name")


class GenreApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]


class ArtistListApiView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class TrackListApiView(generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


# USER:


class CreateUserApiView(CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserPanelApiView(generics.ListAPIView):
    serializer_class = TrackSerializer

    def get_queryset(self):
        user = self.request.user
        return Track.objects.filter(user=user)
