from django.urls import path
from . import views

urlpatterns = [
    path('gestio/', views.gestio_videojocs, name='gestio_videojocs'),
]
