from django.urls import path
from . import views

urlpatterns = [
    path('ArtistListView', views.ArtistListView, name='ArtistList'),
    path('GenreFilterView', views.GenreFilterView, name='GenreFilterView'),
    path('ArtistDetailView', views.ArtistDetailView, name='ArtistDetailView'),
    path('artist_albums', views.artist_albums, name='artist_albums'),
    path('album_detail', views.album_detail, name='album_detail'),
    path('album_songs', views.album_songs, name='album_songs'),
    path('song_detail', views.song_detail, name='song_detail'),
]
