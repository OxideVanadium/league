from django.contrib import admin

from .models import Player


@admin.register(Player)
class Player(admin.ModelAdmin):
    list_display = ['name', 'position']
