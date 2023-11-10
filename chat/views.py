from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import requests
import json
from .models import Texts


def index(request):
    return render(request, 'chat/index.html')


@csrf_exempt
@require_POST
def save_text_to_database(request):
    data = json.loads(request.body)
    input_text = data.get('text', '')

    # Запрос к API Википедии
    wikipedia_api_url = f'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&exintro&titles={input_text}&utf8'
    response = requests.get(wikipedia_api_url)
    json_data = response.json()
    page_id = next(iter(json_data['query']['pages']))

    # Извлечение текста из Википедии (первый абзац)
    output_text = json_data['query']['pages'][page_id]['extract'].split('\n', 1)[0] if 'extract' in \
                                                                                       json_data['query']['pages'][
                                                                                           page_id] else ''

    # Сохранение в базе данных
    text_instance = Texts(input_text=input_text, output_text=output_text)
    text_instance.save()

    return JsonResponse({'status': 'success', 'text_id': text_instance.id, 'output_text': output_text})
