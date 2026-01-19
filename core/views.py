from django.shortcuts import render, redirect
from .forms import SpottedMessageForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SpottedMessage
from decouple import config  
N8N_TOKEN = config('N8N_TOKEN')


def home(request):
    if request.method == 'POST':
        form = SpottedMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SpottedMessageForm()

    return render(request, 'core/home.html', {'form': form})


def get_auth_header(request):
    return request.headers.get("Authorization") or request.META.get("HTTP_AUTHORIZATION")


@csrf_exempt
def new_messages_for_n8n(request):
    auth = get_auth_header(request)

    if auth != f"Bearer {N8N_TOKEN}":
        return JsonResponse({"error": "Unauthorized"}, status=401)

    messages = SpottedMessage.objects.filter(sent_to_n8n=False)
    data = [
        {
            "id": msg.id,
            "text": msg.text,
            "created_at": msg.created_at.isoformat()
        }
        for msg in messages
    ]

    return JsonResponse(data, safe=False)


@csrf_exempt
def mark_message_sent(request, message_id):
    auth = get_auth_header(request)

    if auth != f"Bearer {N8N_TOKEN}":
        return JsonResponse({"error": "Unauthorized"}, status=401)

    try:
        msg = SpottedMessage.objects.get(id=message_id)
        msg.sent_to_n8n = True
        msg.save()
        return JsonResponse({"status": "ok"})
    except SpottedMessage.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)
