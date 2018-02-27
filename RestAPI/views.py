from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max, Min
import json
from .models import *
from .serializers import *
from pytz import UTC
from datetime import datetime, timedelta

@csrf_exempt
def trades(request):
    if request.method == "POST":
        new_trade = json.loads(request.body.decode('utf-8'))

        user, created = User.objects.get_or_create(id=new_trade['user']['id'], name=new_trade['user']['name'])
        try:
            Trade.objects.get(trade_id=int(new_trade['id']))
            # trade id already exists. Send 400 response status
            return JsonResponse({}, status=400)
        except:
            # Send 201 response status
            Trade(id=new_trade['id'], type=new_trade['type'], stock_price= new_trade['stock_price'],
            stock_quantity=new_trade['stock_quantity'], stock_symbol=new_trade['stock_symbol'],
            user=user, trade_timestamp=datetime.strptime(new_trade['trade_timestamp'], "%Y-%m-%d %H:%M:%S").replace(tzinfo=UTC)).save()

        return JsonResponse({}, status=201)
    else:
        tradeSerializer = TradeSerializer(Trade.objects.all().order_by('id'), many=True)
        return JsonResponse(tradeSerializer.data, safe=False)

@csrf_exempt
def trades_user(request, id):
    tradeSerializer = TradeSerializer(Trade.objects.filter(user__id=id), many=True)
    return JsonResponse(tradeSerializer.data, safe=False)


@csrf_exempt
def stock_trades(request, symbol):

    if len(Trade.objects.filter(stock_symbol=symbol)) > 0:
        tradeSerializer = TradeSerializer(Trade.objects.filter(stock_symbol=symbol, type=request.GET['type'],
        trade_timestamp__range=[datetime.strptime(request.GET['start'], "%Y-%m-%d").replace(tzinfo=UTC), datetime.strptime(request.GET['end'], "%Y-%m-%d").replace(tzinfo=UTC) + timedelta(days=1)]).order_by('id'), many=True)
        return JsonResponse(tradeSerializer.data, safe=False)

    return JsonResponse({}, status=404)

@csrf_exempt
def stock_price(request, symbol):
    if len(Trade.objects.filter(stock_symbol=symbol)) > 0:
        prices = Trade.objects.filter(stock_symbol=symbol,
        trade_timestamp__range=[datetime.strptime(request.GET['start'], "%Y-%m-%d").replace(tzinfo=UTC), datetime.strptime(request.GET['end'], "%Y-%m-%d").replace(tzinfo=UTC) + timedelta(days=1)])

        if len(prices) == 0:
            return JsonResponse({"message":"There are no trades in the given date range"})
        else:
            return JsonResponse({"symbol": symbol, "highest_price": prices.aggregate(Max('stock_price'))['stock_price__max'], "lowest_price": prices.aggregate(Min('stock_price'))['stock_price__min']})

    else:
        return JsonResponse({}, status=404)

    return JsonResponse(tradeSerializer.data, safe=False)

@csrf_exempt
def erase(request):
    Trade.objects.all().delete()
    return JsonResponse({})