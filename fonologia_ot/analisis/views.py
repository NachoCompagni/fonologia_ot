from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .utils import generar_candidatos, evaluar_restricciones

def analizar_entrada(request):
    # Obtener la palabra de entrada
    entrada = request.GET.get("entrada", "")

    # Verificar que se ha ingresado la palabra
    if not entrada:
        return HttpResponseBadRequest("No se proporcionó una palabra de entrada.")

    # Obtener el número de candidatos y restricciones
    try:
        num_candidatos = int(request.GET.get("num_candidatos", "1"))
        num_restricciones = int(request.GET.get("num_restricciones", "1"))
    except ValueError:
        return HttpResponseBadRequest("Número de candidatos o restricciones inválido.")

    # Crear una lista dinámica de candidatos
    candidatos = []
    for i in range(1, num_candidatos + 1):
        candidato = request.GET.get(f"candidato_{i}", "")
        if candidato:
            candidatos.append(candidato)
        else:
            return HttpResponseBadRequest(f"Falta el candidato {i}.")

    # Crear una lista dinámica de restricciones
    restricciones = []
    for i in range(1, num_restricciones + 1):
        restriccion = request.GET.get(f"restriccion_{i}", "")
        if restriccion:
            restricciones.append(restriccion)
        else:
            return HttpResponseBadRequest(f"Falta la restricción {i}.")

    # Evaluar restricciones en función de los candidatos generados
    try:
        evaluaciones = evaluar_restricciones(candidatos, restricciones)
    except Exception as e:
        return HttpResponseBadRequest(f"Error al evaluar restricciones: {e}")

    # Encontrar el candidato óptimo (con menor penalización)
    candidato_optimo = min(evaluaciones, key=evaluaciones.get)
    penalizacion_optima = evaluaciones[candidato_optimo]

    # Renderizar la plantilla con los resultados
    return render(request, 'analisis/resultados.html', {
        'entrada': entrada,
        'candidatos': candidatos,
        'restricciones': restricciones,
        'evaluaciones': evaluaciones,
        'candidato_optimo': candidato_optimo,
        'penalizacion_optima': penalizacion_optima
    })



    # restricciones = Restriccion.objects.all()  # Obtiene las restricciones de la base de datos

    # Evaluar restricciones y preparar datos para el template
    # evaluaciones = evaluar_restricciones(candidatos, restricciones)
#     resultados = []
#     for candidato in candidatos:
#         fila_resultado = {
#             'candidato': candidato,
#             'penalizacion': evaluaciones[candidato],
#             'violaciones': [restriccion.violada_por(candidato) for restriccion in restricciones]
#         }
#         resultados.append(fila_resultado)

#     # Encuentra el candidato óptimo (con menor penalización)
#     candidato_optimo = min(evaluaciones, key=evaluaciones.get)
#     penalizacion_optima = evaluaciones[candidato_optimo]

#     return render(request, 'analisis/resultados.html', {
#         'resultados': resultados,
#         'candidato_optimo': candidato_optimo,
#         'penalizacion_optima': penalizacion_optima,
#         'restricciones': restricciones
#     })

def entrada_view(request):
    return render(request, 'analisis/entrada.html')
