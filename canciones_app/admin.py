
from django.contrib import admin
from .models import Artista, Genero, Album, Cancion


@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre", "biografia")
    ordering = ("nombre",)


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "descripcion")
    search_fields = ("nombre", "descripcion")
    ordering = ("nombre",)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "artista", "fecha_lanzamiento")
    list_filter = ("artista",)
    search_fields = ("titulo", "artista__nombre")
    ordering = ("titulo",)


@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "titulo",
        "artista",
        "genero",
        "album",
        "duracion_segundos",
        "destacada",
    )

    list_filter = ("genero", "artista", "destacada")
    search_fields = (
        "titulo",
        "artista__nombre",
        "genero__nombre",
        "album__titulo",
    )

    list_editable = ("destacada",)
    ordering = ("titulo",)
