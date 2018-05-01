from django.shortcuts import render_to_response
from .models import TestBase

def main(request):
    objects = TestBase.objects.all()
    return render_to_response('index.html', {'objects': objects, 'count': objects.count()})

# Create your views here.
