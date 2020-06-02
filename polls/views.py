from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import sport

def home(request):
    all_sport = sport.objects.all()
    return render(request, 'home.html', {'all_sport': all_sport})
