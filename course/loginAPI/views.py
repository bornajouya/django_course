import binascii

from django.shortcuts import render
import sys, os

# Create your views here.
from django.shortcuts import render, HttpResponse
from loginAPI.models import Book, Users, Token
from django.http import JsonResponse
import json
from datetime import datetime, timedelta
from django.db.models import Q
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from random import randint


# Create your views here.
@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            data = request.body.decode("utf-8")
            data = json.loads(data)
            phone_number = data['phone_number']

            randon_valid_key = randint(10000, 99999)

            # send sms

            user = Users(user_phone=phone_number, user_valid_key=str(randon_valid_key))
            user.save()
            return JsonResponse({"info": "user saved"}, safe=False, status=200)


        except:
            return JsonResponse({"info": "internal error"}, safe=False, status=500)


def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()


@csrf_exempt
def confirm(request):
    if request.method == "POST":
        data = request.body.decode("utf-8")
        data = json.loads(data)
        phone_number = data['phone_number']
        validkey = data['valid_key']

        if Users.objects.filter(user_phone=phone_number, user_valid_key="0").exists():
            return JsonResponse({"info": "please login again"}, safe=False, status=401)

        if not Users.objects.filter(user_phone=phone_number).exists():
            return JsonResponse({"info": "user not exist"}, status=404)
        elif not Users.objects.filter(user_phone=phone_number, user_valid_key=validkey).exists():
            return JsonResponse({"info": "wrong valid key"}, status=404)

        Users.objects.filter(user_phone=phone_number, user_valid_key=validkey).update(user_valid_key="0")
        user = Users.objects.get(user_phone=phone_number)
        token = Token(token=generate_key(), user=user)

        token.save()

    return JsonResponse({"info": "ok", "user_token": str(token.token)}, safe=False, status=400)
