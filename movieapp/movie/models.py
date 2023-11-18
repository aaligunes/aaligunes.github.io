from django.db import models
from movie.api import themoviedb


class yorumlar(models.Model):
    yorum = models.TextField(max_length=1000)
    yorum_basligi = models.TextField(max_length=200)
    spoiler = models.BooleanField(default=False)
    yorum_yapilan_film_id = models.IntegerField()
    yorum_yapan_kullanici_adi = models.TextField(max_length=100)
    
    
class favori_filmler(models.Model):
    favori_button = models.BooleanField(default=False)
    favoriye_eklenen_film_id = models.IntegerField()
    favoriye_ekleyen_kullanici_adi = models.TextField(max_length=100)
    