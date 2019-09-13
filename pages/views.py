from django.shortcuts import render
from django.http import HttpResponse

from utils.bnet import Bnet

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
    data = bnet.get_data(token, 'hearthstone/cards/52119-arch-villain-rafaam?locale=en_US')
    return render(request, "viewCards.html", data )
