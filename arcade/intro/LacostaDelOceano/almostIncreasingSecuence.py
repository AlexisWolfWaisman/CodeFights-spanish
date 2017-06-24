"""
Nota: A pesar de parecer simple considero que es un problema complejo si no se tiene el enfoque correcto.

Traduccion del problema: Secuencia casi incremental

Traducccion del enunciado:
    Dada una secuencia de enteros en un arreglo determinar cuando es posible obtener una secuencia estrictamente creciente
    removiendo no mas de un elemento del arreglo.

Enfoque (approach):
    En este caso debemos tener en cuenta que no estamos limitados a usar una sola función.
    Por ende tendremos dos funciones:

    busqueda_disparejo:
        simplemente realiza la operación deseada: busca al elemento que es mayor o igual al siguiente
        devuelve ese elemento cuando lo encuentra o en cualquier otro caso retorna -1.

    almosIncreasingSecuence:
        si el indice es -1 finaliza el programa.
        si el indice no lo es, repite la funcion quitando el indice de la secuencia. (se a quitado un elemento de la secuencia)
        si se repite, se buca la siguiente posicion y se vuelve a comprobar. (se quita un segundo elemento)
        Si no se da ninguno de los anteriores no es la secuencia que buscamos.

PD: La idea a futuro es modificar esté codigo. Usar algo mas comprensible y funcional.
    
"""


def busqueda_disparejo(sequence):
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            return i
    return -1


def almostIncreasingSequence(sequence):
    c = 0
    indice = busqueda_disparejo(sequence)
    if indice == -1:
        return True
    if busqueda_disparejo(sequence[indice - 1:indice] + sequence[indice + 1:]) == -1:
        return True
    if busqueda_disparejo(sequence[indice:indice + 1] + sequence[indice + 2:]) == -1:
        return True
    return False


# El test fue hecho con la idea de verificar los fallos si implementamos diferentes algoritmos.
def test():
    #1
    if (almostIncreasingSequence(  [1, 3, 2] )):
        print("ok")
    else:
        print("revisar el primero")
    #2
    if (almostIncreasingSequence( [10, 1, 2, 3, 4, 5] )):
        print("ok")
    else:
        print("revisar el segundo")
    #3
    if  (almostIncreasingSequence( [0, -2, 5, 6] )): #verdadero
        print("ok")
    else:
        print("revisar el tercero")
    #4
    if not (almostIncreasingSequence([1, 3, 2, 1])):  # falso
        print("ok")
    else:
        print("revisar el cuarto")
    # 5
    if not (almostIncreasingSequence([1, 2, 1, 2] )):  # falso
        print("ok")
    else:
        print("revisar el quinto")
    # 6
    if not (almostIncreasingSequence( [1, 4, 10, 4, 2] )):  # falso
        print("ok")
    else:
        print("revisar el sexto")
    # 7
    if not (almostIncreasingSequence([1, 1, 1, 2, 3])):  # falso
        print("ok")
    else:
        print("revisar el septimo")
    # 8
    if not (almostIncreasingSequence( [40, 50, 60, 10, 20, 30] )):  # falso
        print("ok")
    else:
        print("revisar el octavo")
    # 9
    if  (almostIncreasingSequence( [1, 1] )):  # falso
        print("ok")
    else:
        print("revisar el noveno")
    # 10
    if  (almostIncreasingSequence([1, 2, 3, 4, 3, 6])):  # true
        print("ok")
    else:
        print("revisar el decimo")
test()



