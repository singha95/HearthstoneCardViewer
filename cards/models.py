from django.db import models

# Create your models here.
class Card(models.Model): 
    
    name = models.TextField(max_length=120)
    cost = models.TextField(max_length=120)
    slug = models.TextField(default="", max_length=120)
    image = models.TextField(default="", max_length=120)