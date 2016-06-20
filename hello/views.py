from django.shortcuts import render
from django.http import HttpResponse
# from .models import Greeting
# from django.shortcuts import render
import requests
import populate
import json

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    display_array = json.dumps(populate.populate())
    print display_array
    return render(request, 'index.html',{'data_for_site' : display_array})

#
# def db(request):
#
#     greeting = Greeting()
#     greeting.save()
#
#     greetings = Greeting.objects.all()
# 
#     return render(request, 'db.html', {'greetings': greetings})
