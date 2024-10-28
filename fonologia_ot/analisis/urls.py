from django.urls import path
from . import views

urlpatterns = [
    path('', views.analizar_entrada, name='analizar_entrada'),
    path('entrada/', views.entrada_view, name='entrada'),  # URL de "entrada"
    path('analizar/', views.analizar_entrada, name='analizar_entrada'),
]