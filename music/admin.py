from django.contrib import admin
from .models import Song,Album,Artist

# Register your models here.

admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Artist)
