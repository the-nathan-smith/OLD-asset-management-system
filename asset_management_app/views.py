import re
from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse

def home(request):
    return render(request, "asset_management_app/home.html")

def about(request):
    return render(request, "asset_management_app/about.html")

def contact(request):
    return render(request, "asset_management_app/contact.html")



def hello_there(request, name):
    return render(
        request,
        'asset_management_app/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
