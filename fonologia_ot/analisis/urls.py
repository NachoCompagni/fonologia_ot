from django.urls import path
from . import views

urlpatterns = [
    path('', views.analizar_entrada, name='analizar_entrada'),
]