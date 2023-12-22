from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Song, Album, Artist


# Create your views here.


class ArtistListView(ListView):
    model = Artist
    template_name = 'artist_list.html'
    context_object_name = 'artists'


class GenreFilterView(ListView):
    template_name = 'genre_filter.html'
    context_object_name = 'artists'

    def get_queryset(self):
        genre = self.kwargs['genre']
        return Artist.objects.filter(genre__iexact=genre)


class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'artist_detail.html'
    context_object_name = 'artists'


def artist_albums(request, artist_id):
    albums = Album.objects.filter(artist_id=artist_id)
    return render(request, 'artist_albums.html', {'albums': albums})


def album_detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    return render(request, 'album_detail.html', {'album': album})


def album_songs(request, album_id):
    songs = Song.objects.filter(album_id=album_id)
    return render(request, 'album_songs.html', {'songs': songs})


def song_detail(request, song_id):
    song = Song.objects.get(pk=song_id)
    return render(request, 'song_detail.html', {'song': song})
