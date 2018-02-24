from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *

@csrf_exempt
def trades(request):
    if request.method == "POST":
        new_trade = json.loads(request.body.decode('utf-8'))

        user, created = User.objects.get_or_create(user_id=new_trade['user']['id'], name=new_trade['user']['name'])
        try:
            Trades.objects.get(trade_id=int(new_trade['id']))
            # trade id already exists. Send 400 response status
            return JsonResponse({}, status=400)
        except:
            # Send 201 response status
            Trades(trade_id=new_trade['id'], type=new_trade['type'], stock_price= new_trade['stock_price'], stock_quantity=new_trade['stock_quantity'], stock_symbol=new_trade['stock_symbol'], user=user).save()

        return JsonResponse({}, status=201)
    else:
        return JsonResponse({"trades": "list"})