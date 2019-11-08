from django.shortcuts import render
from .models import experiences

def home(request):
    experience = experiences.objects.all()
    return render(request, 'experiences/home.html', {'experiences':experience})
# Create your views here.
