"""spotify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework import routers

from main_app.views import *
from main_app.api_views import *

router = routers.DefaultRouter()
router.register(r"api/users", UsersViewSet)
router.register(r"api/register", CreateUserApiView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include("rest_framework.urls", namespace="rest_framework")),

    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('dashboard/', DashboardView.as_view()),

    path('addgenre/', GenreAdd.as_view()),
    path('genrelist/', GenreList.as_view()),
    path('genre/<int:id>/', GenreDetails.as_view()),
    path('genre/delete/<pk>/', GenreDelete.as_view()),
    path('genre/update/<pk>/', GenreUpdate.as_view()),

    path('addartist/', ArtistAdd.as_view()),
    path('artistlist/', ArtistList.as_view()),
    path('artist/<int:id>/', ArtistDetails.as_view()),
    path('artist/delete/<pk>/', ArtistDelete.as_view()),
    path('artist/update/<pk>/', ArtistUpdate.as_view()),

    path('addtrack/', TrackAdd.as_view()),
    path('tracklist/', TrackList.as_view()),
    path('track/<int:id>/', TrackDetails.as_view()),
    path('track/delete/<pk>/', TrackDelete.as_view()),
    path('track/update/<pk>/', TrackUpdate.as_view()),

    path('userpanel/', UserPanel.as_view()),
    path('register/', UserRegister.as_view()),
    path('login/', UserLogin.as_view()),
    path('logout/', UserLogout.as_view()),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name="change-password"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name="change-password-done"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name="password-reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name="password-reset-done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password-reset-confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name="password-reset-complete"),

    path('api/genrelist/', GenreListApiView.as_view(), name="genre-list"),
    path('api/genre/<int:pk>/', GenreApiView.as_view(), name="genre-details"),
    path('api/artistlist/', ArtistListApiView.as_view(), name="artist-list"),
    path('api/artist/<int:pk>/', ArtistApiView.as_view(), name="artist-details"),
    path('api/tracklist/', TrackListApiView.as_view(), name="track-list"),
    path('api/track/<int:pk>/', TrackApiView.as_view(), name="track-details"),

    path('api/userpanel/', UserPanelApiView.as_view(), name="usertrack")
]
