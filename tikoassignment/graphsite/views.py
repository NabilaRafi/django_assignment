# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
import requests
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import UserLoginForm

def welcome(request):
    title = "Welcome to Django app"
    return render(request, 'views/welcome.html', {"title": title})

def graph(request):
    title= "Django movie chart"
    return render(request, 'views/graph.html', {"title": title})

def get_joke(request, *args, **kwargs):
    url = 'http://api.icndb.com/jokes/random'
    data = requests.get(url).json()
    return JsonResponse(data)

# Another way of requesting api response through rest framework

# class chartsData(APIView):
#     authentication_classes = []
#     permission_classes = []

#     def get(self, request, format=None):
#         url = 'http://api.icndb.com/jokes'
#         data = requests.get(url).json()
#         return Response(data)
