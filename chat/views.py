from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .models import Audios


# Create your views here.
def index(request):
    return render(request, 'chat/index.html')


@csrf_exempt
@require_POST
def save_text_to_database(request):
    data = json.loads(request.body)
    text_to_save = data.get('text', '')

    # Сохранение текста в базе данных
    audio_instance = Audios(text=text_to_save)
    audio_instance.save()

    return JsonResponse({'status': 'success'})
