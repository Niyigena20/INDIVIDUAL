
from django.shortcuts import render
from web.models import Application

# Create your views here.
def index(request):
    test = Application.objects.all
    page = {'test': test, }
    return render(request, 'index.html', page)

    
    
def details(request):
    test = Application.objects.all
    pg= {'test': test, }
    return render(request, 'details.html', pg)