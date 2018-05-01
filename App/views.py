from django.shortcuts import render
from .models import TestBase

def main(request):
    objects = TestBase.objects.all()
    return render('index.html', {'objects': objects})

# Create your views here.
