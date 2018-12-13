from django.shortcuts import render
from .forms import QueryForm

def index(request):
    response = {'form' : QueryForm}
    return render(request, 'search.html', response)

def query(request):
    query = request.POST['query']
