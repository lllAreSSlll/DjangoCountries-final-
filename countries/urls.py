from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('countries-list/', countries_list, name='countries_list'),
    path('country/<str:country>/', country_info, name='country_info'),
    path('languages/', languages, name='languages'),
    path('language/<str:language>/', language_info, name='language_info'),
    path('countries/alphabet/<str:char>/', countries_list_alphabet, name='countries_list_alphabet'),
]
