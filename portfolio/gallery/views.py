from __future__ import unicode_literals

from django.shortcuts import render
from gallery.models import Gallery

# Create your views here.
def home(request,):
    gallerys = Gallery.objects.all()
    print(gallerys)
    return render(request, 'home.html', {'gallerys':gallerys})

def home2(request):
    gallerys = Gallery.objects.all()
    return render(request, 'home2.html', {'gallerys':gallerys})