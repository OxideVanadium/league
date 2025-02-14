# Create your models here.
from django.db import models


class Player(models.Model):
    class Position(models.TextChoices):
        GOALKEEPER = 'G', 'Goalkeeper'
        DEFENSE = 'D', 'Defender'
        MIDFIELDER = 'M', 'Midfielder'
        FORWARD = 'F', 'Forward'

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    position = models.CharField(choices=Position, max_length=1)
    birth_date = models.DateField()
    market_value = models.DecimalField(max_digits=8, decimal_places=2)
    photo = models.ImageField(blank=True, null=True, default='players/photos/default.png')
    team = models.ForeignKey(
        'teams.Team', on_delete=models.SET_NULL, related_name='team', null=True
    )

    def __str__(self):
        return self.name
