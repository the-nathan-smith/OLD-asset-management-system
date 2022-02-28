import re
from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")


def hello_there(request, name):
    return render(
        request,
        'asset_management_app/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
