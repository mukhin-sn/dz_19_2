
from django.urls import path
from catalog.views import *

urlpatterns = [
    path('', my_controller_1),
    path('contacts/', my_controller_2),
]