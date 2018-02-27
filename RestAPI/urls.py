from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^trades/$', trades, name="trades"),
    url(r'^trades/users/(?P<id>\d+)', trades_user, name="trades_user"),
    url(r'^stocks/(?P<symbol>\w+)/trades', stock_trades, name="stock_trades"),
    url(r'^stocks/(?P<symbol>\w+)/price', stock_price, name="stock_price"),
    url(r'^erase/', erase, name="erase"),
]
