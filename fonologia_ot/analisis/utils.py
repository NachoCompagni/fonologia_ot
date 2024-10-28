def generar_candidatos(entrada):
    """
    Genera automáticamente posibles candidatos a partir de una entrada fonológica.
    Puedes modificar esta función para adaptarla a variaciones fonológicas específicas.
    """
    candidatos = []
    for variante in ["var1", "var2", "var3"]:  # Ejemplo de variantes, ajusta según las reglas de fonología
        candidatos.append(f"{entrada}_{variante}")
    return candidatos

def evaluar_restricciones(candidatos, restricciones):
    """
    Evalúa cada candidato en función de las restricciones y asigna penalizaciones.
    Los candidatos que violen una restricción suman el peso de la restricción a su penalización total.
    """
    evaluaciones = {}
    for candidato in candidatos:
        penalizaciones = 0
        for restriccion in restricciones:
            if restriccion.violada_por(candidato):  # Método personalizado para verificar violaciones
                penalizaciones += restriccion.peso
        evaluaciones[candidato] = penalizaciones
    return evaluaciones
