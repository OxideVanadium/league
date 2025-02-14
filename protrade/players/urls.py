from django.urls import path

from . import views

app_name = 'players'

urlpatterns = [
    path('', views.player_list, {'method': 'GET'}, name='game-player-list'),
    path(
        'add/',
        views.add_player,
        {
            'method': 'POST',
            'fields': ['name', 'slug', 'position', 'birth-date', 'market-value', 'team-slug'],
        },
        name='add-player',
    ),
    path(
        'transfer/',
        views.transfer_player,
        {'method': 'POST', 'fields': ['player-slug', 'team-slug']},
        name='transfer-player',
    ),
    path('<str:slug>/', views.player_detail, {'method': 'GET'}, name='player-detail'),
]
