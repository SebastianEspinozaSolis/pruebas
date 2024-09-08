from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('primerosPasos/', views.vista1),
    path('vistasApps/', views.vista2),
]