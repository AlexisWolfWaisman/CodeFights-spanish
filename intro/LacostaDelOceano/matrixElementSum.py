"""
Traduccion del problema: Suma de elementos en una matriz

Traducccion del enunciado:

    Despues de volverse famoso el equipo de CodeBots , decidio mudarse a un nuevo edificio para vivir en comunidad.
    en este caso el edificio esta representado por una matriz rectangular de cuartos representados por celdas de la matriz, cada celda contiene un entero
    (el precio del cuarto). Algunos cuartos son gratuitos (costo 0), pero esto es debido a que probablemente estan embrujadas :-S
    los miembros del equipo temen estar en estas habitaciones. Esta es la Razon de porque son gratuitas, y consecuentemente todas las habitaciones por debajo
    de está en la misma columna no son consideradas habitables para nuestros bots (miembros del equipo).
    Ayuda a los bots a calcular el costo total de todos los cuartos disponibles para ellos.

    | H , H , H |
    | H , E , H |
    | H , In, H |

    H --> Habitable
    E --> Embrujada
    In --> Inhabitable


Enfoque (approach):
    Dado que nos dan la matriz de pisos (filas):
    1) recorrer la matriz por columnas (No por filas)
    2) si hallamos un cuarto de coste 0, suspendemos la sumatoria.
"""
def matrixElementsSum(matrix):
    i = len(matrix)
    j = len(matrix[0])
    total = 0
    for y in range(0, j):
        vector = []
        for x in range(0,i):
            vector.append(matrix[x][y])
        for elem in vector:
            if elem == 0:
                break
            else:
                total += elem
    return total

def test():
    # se prueban con los elementos dados en el area de testing de la plataforma
    prueba1 = [[0, 1, 1, 2],[0, 5, 0, 0],[2, 0, 3, 3]]
    prueba2 = [[1,1,1,0],[0,5,0,1],[2,1,3,10]]

    print(matrixElementsSum(prueba1))
    print(matrixElementsSum(prueba2))

test()


