import json
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def getRoutes(request):
    return JsonResponse('our api',safe=False);
    #safe means we can return more data than python dictionart