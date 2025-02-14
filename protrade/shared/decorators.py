import json
import re

from django.http import JsonResponse
from users.models import Token


def method_check(func):
    def wrapper(*args, **kwargs):
        if args[0].method == kwargs['method']:
            return func(*args, **kwargs)
        return JsonResponse({'error': 'Method not allowed'}, status=405)

    return wrapper


def json_check(func):
    def wrapper(*args, **kwargs):
        try:
            json_data = json.loads(args[0].body)
            if fields := kwargs['fields']:
                for field in fields:
                    if not json_data.get(field, None):
                        return JsonResponse({'error': 'Missing required fields'}, status=400)
            return func(json_data=json_data, *args, **kwargs)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON body'}, status=400)

    return wrapper


def user_check(func):
    def wrapper(*args, **kwargs):
        pattern = r'^Bearer ([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$'
        match = re.match(pattern, args[0].headers.get('Authorization'))
        if match:
            token = match.group(1)
            try:
                Token.objects.get(key=token)
                return func(*args, **kwargs)
            except Token.DoesNotExist:
                return JsonResponse({'error': 'Unregistered authentication token'}, status=401)
        return JsonResponse({'error': 'Invalid authentication token'}, status=400)

    return wrapper
