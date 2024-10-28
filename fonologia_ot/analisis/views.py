from django.shortcuts import render
from .utils import generar_candidatos, evaluar_restricciones
from .models import Restriccion

def analizar_entrada(request):
    entrada = request.GET.get("entrada", "")
    candidatos = generar_candidatos(entrada)
    restricciones = Restriccion.objects.all()  # Obtiene las restricciones de la base de datos

    # Evaluar restricciones y preparar datos para el template
    evaluaciones = evaluar_restricciones(candidatos, restricciones)
    resultados = []
    for candidato in candidatos:
        fila_resultado = {
            'candidato': candidato,
            'penalizacion': evaluaciones[candidato],
            'violaciones': [restriccion.violada_por(candidato) for restriccion in restricciones]
        }
        resultados.append(fila_resultado)

    # Encuentra el candidato óptimo (con menor penalización)
    candidato_optimo = min(evaluaciones, key=evaluaciones.get)
    penalizacion_optima = evaluaciones[candidato_optimo]

    return render(request, 'analisis/entrada.html', {
        'resultados': resultados,
        'candidato_optimo': candidato_optimo,
        'penalizacion_optima': penalizacion_optima,
        'restricciones': restricciones
    })

def entrada_view(request):
    return render(request, 'analisis/entrada.html')
