from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, World!')


def about(request):
    return HttpResponse('I am the static pages generator')
