# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.test import TestCase
from rest_framework.test import RequestsClient
import json
from dateutil.parser import parse


class RestTestCase(TestCase):

    def setUp(self):
        self.test_1 = []
        self.test_2 = []
        self.test_3 = []
        self.test_4 = []
        with open('TestData/http00.json') as f:
            for line in f:
                self.test_1.append(line)
        with open('TestData/http01.json') as f:
            for line in f:
                self.test_2.append(line)
        with open('TestData/http02.json') as f:
            for line in f:
                self.test_3.append(line)
        with open('TestData/http03.json') as f:
            for line in f:
                self.test_4.append(line)

    def test_get_all_trades(self):
        client = RequestsClient()
        for ro in self.test_1:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                res = client.get('http://localhost:8000' +
                                 row['request']['url'] + '/')
            elif row['request']['method'] == "POST":
                res = client.post(
                    'http://localhost:8000' + row['request']['url'] + '/', json=row['request']['body'])
            elif row['request']['method'] == "DELETE":
                res = client.delete(
                    'http://localhost:8000' + row['request']['url'] + '/')
            self.assertEqual(res.status_code, row['response']['status_code'])
            if row['response']['headers'] != {}:
                self.assertEqual(
                    res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            if row['response']['body'] != {}:
                response = json.loads(res.text)
                for resp in response:
                    if resp['trade_timestamp']:
                        temp = parse(resp['trade_timestamp'])
                        temp = temp.replace(tzinfo=None)
                        temp = str(temp)
                        resp['trade_timestamp'] = temp
                self.assertEqual(response, row['response']['body'])

    def test_get_trades_by_user_id(self):
        client = RequestsClient()
        for ro in self.test_2:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                res = client.get('http://localhost:8000' +
                                 row['request']['url'] + '/')
            elif row['request']['method'] == "POST":
                res = client.post(
                    'http://localhost:8000' + row['request']['url'] + '/', json=row['request']['body'])
            elif row['request']['method'] == "DELETE":
                res = client.delete(
                    'http://localhost:8000' + row['request']['url'] + '/')
            self.assertEqual(res.status_code, row['response']['status_code'])
            if row['response']['headers'] != {}:
                self.assertEqual(
                    res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            if row['response']['body'] != {}:
                response = json.loads(res.text)
                for resp in response:
                    if resp['trade_timestamp']:
                        temp = parse(resp['trade_timestamp'])
                        temp = temp.replace(tzinfo=None)
                        temp = str(temp)
                        resp['trade_timestamp'] = temp
                self.assertEqual(response, row['response']['body'])

    def test_get_trades_by_trade_type(self):
        client = RequestsClient()
        for ro in self.test_3:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                res = client.get('http://localhost:8000' +
                                 row['request']['url'] + '/')
            elif row['request']['method'] == "POST":
                res = client.post(
                    'http://localhost:8000' + row['request']['url'] + '/', json=row['request']['body'])
            elif row['request']['method'] == "DELETE":
                res = client.delete(
                    'http://localhost:8000' + row['request']['url'] + '/')
            self.assertEqual(res.status_code, row['response']['status_code'])
            if row['response']['headers'] != {}:
                self.assertEqual(
                    res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            if row['response']['body'] != {}:
                response = json.loads(res.text)
                for resp in response:
                    if resp['trade_timestamp']:
                        temp = parse(resp['trade_timestamp'])
                        temp = temp.replace(tzinfo=None)
                        temp = str(temp)
                        resp['trade_timestamp'] = temp
                self.assertEqual(response, row['response']['body'])

    def test_get_stock_price(self):
        client = RequestsClient()
        for ro in self.test_3:
            row = json.loads(ro)
            res = {}
            if row['request']['method'] == "GET":
                res = client.get('http://localhost:8000' +
                                 row['request']['url'] + '/')
            elif row['request']['method'] == "POST":
                res = client.post(
                    'http://localhost:8000' + row['request']['url'] + '/', json=row['request']['body'])
            elif row['request']['method'] == "DELETE":
                res = client.delete(
                    'http://localhost:8000' + row['request']['url'] + '/')
            self.assertEqual(res.status_code, row['response']['status_code'])
            if row['response']['headers'] != {}:
                self.assertEqual(
                    res.headers['Content-Type'], row['response']['headers']['Content-Type'])
            if row['response']['body'] != {}:
                response = json.loads(res.text)
                for resp in response:
                    if resp['trade_timestamp']:
                        temp = parse(resp['trade_timestamp'])
                        temp = temp.replace(tzinfo=None)
                        temp = str(temp)
                        resp['trade_timestamp'] = temp
                self.assertEqual(response, row['response']['body'])
