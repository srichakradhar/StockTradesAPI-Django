from django.db import models
from django.utils import timezone

class User(models.Model):
    user_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=64)

class Trades(models.Model):
    TRADE_TYPES = (
        ('buy', 'Buy'),
        ('sell', 'Sell')
    )
    trade_id = models.IntegerField(unique=True)
    type = models.CharField(max_length=4, choices=TRADE_TYPES)
    user = models.ForeignKey(User)
    stock_symbol = models.CharField(max_length=5)
    stock_quantity = models.IntegerField(default=0)
    stock_price = models.DecimalField(decimal_places=2, max_digits=12)
    trade_timestamp = models.DateTimeField(default = timezone.now)