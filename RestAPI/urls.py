from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^trades/', trades, name="trades"),
]
