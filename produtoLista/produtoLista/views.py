from django.shortcuts import render
from django.http import HttpResponse


def lista_produtos(request):
    return render(request, "index.html")