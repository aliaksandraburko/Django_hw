from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class MusicBand(models.Model):
    name_band = models.CharField(max_length=255, default=None)
    year_of_foundation= models.CharField(max_length=255, default=None)

    musical_style = models.CharField(max_length=255, default=None)

    def __str__(self):
        return f'{self.pk}{self.name_band}'


class Album(models.Model):
    name_album = models.CharField(max_length=255, default=None)
    year_of_issue = models.CharField(max_length=255, default=None)
    group = models.ForeignKey('MusicBand', null=True, on_delete=models.SET_NULL, related_name='groups', )

    def __str__(self):
        return f'{self.pk} {self.name_album}'


class Track(models.Model):
    title = models.CharField(max_length=255, default=None)
    duration = models.CharField(max_length=255, default=None)
    which_albums = models.OneToOneField(
        Album, null=True,
        related_name='tracks',
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f'{self.pk} {self.title}'