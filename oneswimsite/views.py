from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {"hello": 'one swim'}
    return render(request, "index.html", context)
