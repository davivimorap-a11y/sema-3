
from django.db import models


class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField(blank=True)
    foto_url = models.URLField(
        blank=True,
        verbose_name="Foto del cantante"
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artistas"
        ordering = ["nombre"]


class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ["nombre"]


class Album(models.Model):
    titulo = models.CharField(max_length=150)
    artista = models.ForeignKey(
        Artista,
        on_delete=models.CASCADE,
        related_name="albumes",
        verbose_name="Cantante"
    )
    portada_url = models.URLField(
        blank=True,
        verbose_name="Portada del álbum"
    )
    fecha_lanzamiento = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.titulo} - {self.artista.nombre}"

    class Meta:
        verbose_name = "Álbum"
        verbose_name_plural = "Álbumes"
        ordering = ["titulo"]


class Cancion(models.Model):
    titulo = models.CharField(max_length=150)

    artista = models.ForeignKey(
        Artista,
        on_delete=models.CASCADE,
        related_name="canciones",
        verbose_name="Cantante"
    )

    genero = models.ForeignKey(
        Genero,
        on_delete=models.PROTECT,
        related_name="canciones",
        verbose_name="Género musical"
    )

    album = models.ForeignKey(
        Album,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="canciones",
        verbose_name="Álbum"
    )

    portada_url = models.URLField(
        blank=True,
        verbose_name="Portada de la canción"
    )

    archivo_audio = models.FileField(
        upload_to="canciones/",
        blank=True,
        verbose_name="Archivo de audio"
    )

    duracion_segundos = models.PositiveIntegerField(
        default=0,
        verbose_name="Duración en segundos"
    )

    fecha_publicacion = models.DateField(
        null=True,
        blank=True
    )

    destacada = models.BooleanField(
        default=False,
        verbose_name="Canción destacada"
    )

    def __str__(self):
        return f"{self.titulo} - {self.artista.nombre}"

    class Meta:
        verbose_name = "Canción"
        verbose_name_plural = "Canciones"
        ordering = ["titulo"]
