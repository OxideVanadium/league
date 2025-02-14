from django.contrib import admin

from .models import Team


@admin.register(Team)
class Team(admin.ModelAdmin):
    list_display = ['name', 'league']
