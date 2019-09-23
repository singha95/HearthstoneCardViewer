from django.contrib import admin
from django.urls import path
from django.urls import re_path

from pages.views import home_view, cards_view, get_cards_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('cards/', cards_view, name="cards"),
    re_path(r'^cards/results/$', get_cards_search, name="search")
]
