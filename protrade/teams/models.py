from django.db import models


class Team(models.Model):
    class League(models.TextChoices):
        LALIGA = 'L', 'Laliga'
        PREMIER = 'P', 'Premier'
        CALCIO = 'C', 'Calcio'
        BUNDESLIGA = 'B', 'Bundesliga'

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    shield = models.ImageField(blank=True, null=True, default='teams/shields/default.png')
    league = models.CharField(choices=League, max_length=1)

    def __str__(self):
        return self.name
