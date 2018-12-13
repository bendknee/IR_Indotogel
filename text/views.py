from django.shortcuts import render


def index(request):
    response = {}
    return render(request, 'search.html', response)
