from itertools import product

# Generar todas las posibles combinaciones de votos para los 3 grupos
# Cada grupo puede tener entre 0 y 3 votos de cada tipo, sin exceder el total
votos_posibles = [10, 8, 6]
combinaciones_tribunal = list(product(votos_posibles, repeat=3))

# Usaremos un conjunto para almacenar combinaciones únicas
combinaciones_validas = set()

# Filtrar combinaciones para asegurar que no se exceda el número de votos de cada tipo
for comb in product(combinaciones_tribunal, repeat=3):
    votos = [voto for grupo in comb for voto in grupo]
    if votos.count(10) == 3 and votos.count(8) == 3 and votos.count(6) == 3:
        # Convertimos la tupla a una tupla ordenada para que las entradas no se repitan
        comb_ordenada = tuple(sorted(comb))
        combinaciones_validas.add(comb_ordenada)


# Definir el número total de votos de cada tipo
total_10 = 12
total_8 = 12

# Inicializar la lista para almacenar las combinaciones válidas
combinaciones_participantes = []

# Calcular todas las posibilidades de distribuir los 12 votos de 10 entre los 3 grupos
for grupo_10_1 in range(total_10 + 1):
    for grupo_10_2 in range(total_10 + 1):
        for grupo_10_3 in range(total_10 + 1):
            if grupo_10_1 + grupo_10_2 + grupo_10_3 == total_10:  # Verificar que se distribuyan los 12 votos de 10
                # Calcular el número de votos de 8 en cada grupo para completar los 8 votos totales
                votos_8_grupo_1 = 8 - grupo_10_1
                votos_8_grupo_2 = 8 - grupo_10_2
                votos_8_grupo_3 = 8 - grupo_10_3
                # Verificar que los votos de 8 sean no negativos y no excedan los 12 votos disponibles
                if 0 <= votos_8_grupo_1 <= total_8 and 0 <= votos_8_grupo_2 <= total_8 and 0 <= votos_8_grupo_3 <= total_8:
                    # Verificar que la distribución sea diferente para todos los grupos
                    if (grupo_10_1, grupo_10_2, grupo_10_3, votos_8_grupo_1, votos_8_grupo_2, votos_8_grupo_3) not in combinaciones_participantes:
                        combinaciones_participantes.append((grupo_10_1, grupo_10_2, grupo_10_3, votos_8_grupo_1, votos_8_grupo_2, votos_8_grupo_3))


def calcular_resultado(combinacion_valida, combinacion_participante):
    resultado_grupo = []
    for i in range(3):  # Iterar sobre los tres grupos
        puntos_grupo = sum(combinacion_valida[i]) * 0.8  # Calcular puntos basados en combinación válida
        # Añadir votos de 10 y 8 a los puntos del grupo
        puntos_grupo += combinacion_participante[i] * 10 * 0.2 + combinacion_participante[i+3] * 8 * 0.2
        resultado_grupo.append(round(puntos_grupo, 1))  # Agregar resultado con un decimal
    return resultado_grupo

# Define los resultados finales para cada grupo
final_results = {
    "CU001": 29.6,
    "CU002": 36,
    "TLR01": 35.2
}

# Variable para contar el número total de opciones
total_resultados = 0

# Recorrer todas las combinaciones válidas e imprimir los resultados si coinciden con los resultados finales
for comb_valida in combinaciones_validas:
    for comb_participante in combinaciones_participantes:
        resultado = calcular_resultado(comb_valida, comb_participante)
        # Verificar si el resultado coincide con los resultados finales
        if resultado[0] == final_results["CU001"] and resultado[1] == final_results["CU002"] and resultado[2] == final_results["TLR01"] and comb_valida[0] == (6, 6, 6):
            print("Combinación válida:", comb_valida)
            print("Combinación participante:", comb_participante)
            print("Resultado para cada grupo:", resultado)
            total_resultados += 1

print("Número total de opciones:", total_resultados)
