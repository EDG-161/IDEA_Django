import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from . import logic
from django.shortcuts import render


@csrf_exempt
def home(request):
    return render(request, 'plano.html')


@csrf_exempt
def cypher(request):
    logs = []
    if request.method == 'POST':
        key_generator = logic.key_schedule(request.POST.get('password'))
        keys = key_generator["keys"]
        logs.append(key_generator["logs"])
        cypher_result = logic.encrypt(request.POST.get('text'), keys)
        cypher = cypher_result['cypher_text']
        logs.append(cypher_result["logs"])
        response = {
            'cypher_text': cypher,
            'logs': logs
        }
    else:
        text = "hola"
        password = "password"
        key_generator = logic.key_schedule(password)
        keys = key_generator["keys"]
        logs.append(key_generator["logs"])
        cypher_result = logic.encrypt(text, keys)
        cypher = cypher_result['cypher_text']
        logs.append(cypher_result["logs"])
        response = {
            'cypher_text': cypher,
            'logs': logs
        }
    return HttpResponse(
        json.dumps(response),
        content_type='application/javascript; charset=utf8'
    )


@csrf_exempt
def decrypt(request):
    logs = []
    if request.method == 'POST':
        try:
            key_generator = logic.key_schedule(request.POST.get('password'))
            keys = key_generator["keys"]
            decryption_keys = logic.decription_keys_scheduling(keys)
            logs.append(key_generator["logs"])
            decrypted = logic.decrypt(request.POST.get('text'), decryption_keys)
            response = {
                'decrypted_text': decrypted,
                'logs': logs
            }
        except:
            response = {
                'decrypted_text': "Texto no valido",
                'logs': logs
            }
    else:
        response = {
            'cypher_text': "cypher",
            'logs': ""
        }
    return HttpResponse(
        json.dumps(response),
        content_type='application/javascript; charset=utf8'
    )


def index(request):
    pass
