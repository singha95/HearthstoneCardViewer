from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

import json
from utils.bnet import Bnet
from cards.models import Card

import os 


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Create your views here.
def home_view(request, *args, **kwargs): 
    #return HttpResponse("<h1> hellow World</h1>")
    my_context = { 
        "my_text": "This is the homepage"
    }
    return render(request, "home.html", my_context)

def cards_view(request, *args, **kwargs): 
    #return HttpResponse("<h1> hellow World</h1>")
    bnet = Bnet()
    token = bnet.generate_token()
    data = bnet.get_data(token, 'hearthstone/cards?locale=en_US')
    return render(request, "viewCards.html", data )

def get_cards_search(request, *args, **kwargs): 
    url = request.get_full_path()
    name_search = url.split("=")[1]
    cards_json = json.loads(serializers.serialize("json", Card.objects.filter(name__contains=name_search)))
    cards_json = [ x["fields"] for x in cards_json ]
    data = { "cards" : cards_json}
    return render(request, "viewCards.html", data ) 
