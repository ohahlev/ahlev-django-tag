from django.shortcuts import render


def index(request):
    return HttpResponse("this is index of tag app")
