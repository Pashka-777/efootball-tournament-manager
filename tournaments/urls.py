from django.urls import path
from . import views

urlpatterns = [
    path('', views.tournament_list, name='tournament_list'),
    path('create/', views.tournament_create, name='tournament_create'),
]