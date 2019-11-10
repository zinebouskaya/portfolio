from django.shortcuts import render
from .models import experiences

def home(request):
    experience = experiences.objects
    return render(request, 'experiences/home.html', {'experience':experience})
# Create your views here.
