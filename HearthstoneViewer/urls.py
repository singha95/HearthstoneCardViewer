from django.contrib import admin
from django.urls import path

from pages.views import home_view, cards_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('cards/', cards_view)
]
