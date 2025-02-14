import re
from datetime import date

from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shared.decorators import json_check, method_check, user_check
from teams.models import Team

from .models import Player
from .serializers import PlayerSerializer


@method_check
def player_list(request, method):
    players = Player.objects.all()
    if position := request.GET.get('position'):
        players = players.filter(position=position)
    if team := request.GET.get('team'):
        players = players.filter(team__slug=team)
    data = PlayerSerializer(players, request=request)
    return data.json_response()


@method_check
def player_detail(request, slug, method):
    try:
        player = Player.objects.get(slug=slug)
        data = PlayerSerializer(player, request=request)
        return data.json_response()
    except Player.DoesNotExist:
        return JsonResponse({'error': 'Player not found'}, status=404)


@csrf_exempt
@method_check
@json_check
@user_check
def add_player(request, method, fields, json_data):
    if (position := json_data['position']) not in Player.Position:
        return JsonResponse({'error': 'Invalid position'}, status=400)
    if not re.fullmatch(r'^\d{4}-\d{2}-\d{2}$', birth_date := json_data['birth-date']):
        return JsonResponse({'error': 'Invalid birth date'}, status=400)
    try:
        team = Team.objects.get(slug=json_data['team-slug'])
        player = Player.objects.create(
            name=json_data['name'],
            slug=json_data['slug'],
            position=position,
            birth_date=date.fromisoformat(birth_date),
            market_value=float(json_data['market-value']),
            team=team,
        )
        player.save()
        return JsonResponse({'id': player.pk}, status=200)
    except Team.DoesNotExist:
        return JsonResponse({'error': 'Team not found'}, status=400)
    except IntegrityError:
        return JsonResponse({'error': 'Player already exists'}, status=400)


@csrf_exempt
@method_check
@json_check
@user_check
def transfer_player(request, method, fields, json_data):
    try:
        player = Player.objects.get(slug=json_data['player-slug'])
        team = Team.objects.get(slug=json_data['team-slug'])
        if player.team.league != team.league:
            player.market_value = float(player.market_value) * 1.1
        player.team = team
        player.save()
        return JsonResponse({'id': player.pk}, status=200)
    except Player.DoesNotExist:
        return JsonResponse({'error': 'Player not found'}, status=400)
    except Team.DoesNotExist:
        return JsonResponse({'error': 'Team not found'}, status=400)
