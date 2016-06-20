from django.shortcuts import render
from django.http import HttpResponse
import requests
import populate
import json

# Create your views here.
def index(request):
    display_array = json.dumps(populate.populate())
    print display_array
    return render(request, 'index.html',{'data_for_site' : display_array})
