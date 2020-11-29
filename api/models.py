# models.py
from django.db import models

SPECTRAL_CLASS = [("O", "O"), ("B", "B"), ("A", "A"),
                  ("F", "F"), ("G", "G"), ("K", "K"),
                  ("M", "M"), ("L", "L"), ("T", "T"),
                  ("Y", "Y")]


class Star (models.Model):
    id = models.BigIntegerField(primary_key = True)
    name = models.CharField(max_length=30)
    star_system = models.CharField(max_length=30)
    distance = models.FloatField()
    year_of_discovery = models.IntegerField(blank=True, default=None, null=True)
    apparent_magnitude = models.FloatField(blank=True, default=None, null=True)
    absolut_magnitude = models.FloatField(blank=True, default=None, null=True)
    spectral_class = models.CharField(max_length=1, choices=SPECTRAL_CLASS)
    parallax = models.FloatField(blank=True, default=None, null=True)

    def __str__(self):
        return self.name
