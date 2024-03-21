# Calculadora de Resultados de Votos

Esta calculadora de resultados de votos es una herramienta que permite calcular y filtrar las posibles combinaciones de resultados de votos para diferentes grupos, dadas ciertas restricciones y condiciones.

## Restricciones

Las restricciones para las combinaciones de votos son las siguientes:

### tribunales
- Cada integrante del tribunal tiene un voto de 10, un voto de 8 y un voto de 6.
- Cada integrante del tribunal puede usar una sola vez cada voto.
- El total de votos que debe recibir un equipo siempre será de 3.
### Participantes
- Para simplificar, los equipos no votan.
- Se distribuyen el total de votos, es decir 24 votos, entre los 3 equipos, cada equipo contará con 8 votos.
- hay 12 votos de 10 puntos, y 12 votos de 8 puntos que deberán ser distribuidos

## Funcionamiento del Código

### Generación de Combinaciones Válidas

El código comienza generando todas las posibles combinaciones de votos de los tribunales para los 3 grupos, asegurándose de que cumplan con las restricciones mencionadas anteriormente.

### Generación de Combinaciones de Participantes

Luego, se calculan todas las posibilidades de distribuir los 12 votos de 10 y 12 votos de 8 entre los 3 grupos.

### Cálculo de Resultados

Para cada combinación válida y combinación de participantes, se calculan los resultados para cada grupo según la fórmula especificada, que tiene en cuenta los votos de 10 y 8 asignados a cada grupo.

### Filtrado de Resultados

Los resultados se filtran para garantizar que no se repitan combinaciones exploradas ya que en el voto de los tribunales no nos importa el orden ( lo mismo es (10,8,6) que (6,8,10)). Se utilizan conjuntos para mantener un registro de las combinaciones de votos ya exploradas para cada grupo y las combinaciones de participantes.

## Ejecución del Código

El código puede ejecutarse en cualquier entorno de Python 3.x. No requiere dependencias externas.

Para ejecutar el código, simplemente ejecuta el archivo `main.py`. Asegúrate de tener Python 3.x instalado en tu sistema.

