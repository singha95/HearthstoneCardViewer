from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs): 
    #return HttpResponse("<h1> hellow World</h1>")
    my_context = { 
        "my_text": "This is the homepage"
    }
    return render(request, "home.html", my_context)
