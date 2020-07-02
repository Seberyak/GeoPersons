from django.shortcuts import render
from API.views import create_person
import json

def index(request):
    p = create_person()[0]
    person = {
        "first_name_ge": p['first_name'][0],
        "first_name_eng": p['first_name'][1][0].upper()+p['first_name'][1][1:],
        "last_name_ge": p['last_name'][0],
        "last_name_eng": p['last_name'][1][0].upper()+p['last_name'][1][1:],
        "email": p['email'],
        "date_of_birth": p['date_of_birth'],
        "password": p['password'],
        "url": "geopersons.herokuapp.com/api/"

    }
    print(p)
    return render(request, 'GeoPerson/index.html', person)
