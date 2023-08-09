from django.urls import path
from .views import *

urlpatterns = [
    path('', base, name='base'),
    path('home/', home, name='home'),
    path('download/<int:id>', download, name='download'),



]