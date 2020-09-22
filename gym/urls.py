from django.urls import path
from . import views
urlpatterns = [
    path("" , views.index,name='gymhome'),
    path("fitness/" , views.fitness,name='fitness'),
    path("service/" , views.service,name='service'),
    path("about/" , views.about,name='about'),
    path("contact/" , views.contact,name='gymhome'),
    path("thank/" , views.thank,name='thank'),
]
