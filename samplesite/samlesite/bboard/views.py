"""Контроллер(view) Django - это код, запускаемый в ответ на поступление 
клиенского запроса """

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return HttpResponse("Здесь будет выведен список объявлений.")
