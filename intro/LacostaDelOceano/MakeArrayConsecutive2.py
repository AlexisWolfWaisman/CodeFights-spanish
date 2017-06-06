"""
Traduccion del problema: Construir un arreglo de 2-consecutivos

Traducccion del enunciado:
    Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.
    Ratiorg obtuvo estatuas de diferentes tamaños como un obsequio de CodeMaster para su cumpleaños,
    cada estatua tiene un tamaño que se traduce en un entero no-negativo; Como él es perfeccionista, desea ordenarlos
    de menor a mayor de manera tal que cada estatua sea exactamente mas grande que la anterior en una unidad, podría necesitar
    algunas estatuas adicionales para tal cometido, ayudalo a descubrir el numero de estatuas adicionales necesarias.


Enfoque (approach):
    1) Si contamos dentro del rango de tamaños de las estatuas los enteros que faltan habremos resuelto el problema.
    PD: no es necesario ordenar el arreglo
"""

def makeArrayConsecutive2(statues):
    minimalNumberOfStatues = 0
    for i in range(min(statues),max(statues)):
        if i not in statues:
            minimalNumberOfStatues += 1
    return minimalNumberOfStatues

def test():
    print(makeArrayConsecutive2([6, 2, 3, 8]))
    print(makeArrayConsecutive2([0,3]))
    print(makeArrayConsecutive2([5,4,6]))
    print(makeArrayConsecutive2([6, 3]))
    print(makeArrayConsecutive2([1]))

test()
