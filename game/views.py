from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    a=75
    return render(request, 'game/index.html',{'abc':a})
