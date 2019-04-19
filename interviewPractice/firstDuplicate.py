"""
Primer duplicado (FirstDuplicate)
<English>
The goal of this algorithm is to priorize optimization (because we can achieve the same results ia a "greedy" way).
knowing that the maximum value that any item in the list can have is the length of the list. this fact  will allow us to index using it own values as reference for indexation.

Hence the approach is:
Given a list with values ranging from 1 to len(list) [list length], we will mark the  positions related each element in the secuence, making them negative . In this way if there is a 3 , its respective position is  index 2 (remember that lists start at zero). This marking is done successively until a negative value is found... In that case we solved the enigma. :-D

Process
eval each element from the list, if it is negative , this is the "marked"-one  (the one we look for and that we previously mark) if it is not , qe have to to mark its corresponding index in the list.

given the array/list = [4,1,4,3,2,1] at a glance 4 is the answer...

the algorithm will evaluate the first value: 4.
- is it negative? (given that it is the first case... the question is a little silly  but later it will make sense)
- No, it is positive, so the position 0 (which is the index - 1) will be marked as negative.
- but this will be a problem latter? .
- No, because we are always looking for the absolute value, despite working with integers.

1° iteration
item = 4 (the first)
a = [4,1,4,-3,2,1] we mark the item whose index is 4-1... 3.

2nd iteration
item = 1 (the second)
a = [-4,1,4,-3,2,1] we mark the element whose index is 1-1...the element in position 0 is marked.

3rd iteration
item = 4 (the third)
a = [-4,1,4,-3,2,1]
the function will evaluate if it is positive a[4-1] = a[3] = -4... and is not so Bingo! The "marked".

in this case the function returns -4 * -1 (because the focus is on the index) but instead you can use the fabs return or simply the item... the result will be 4, as we knows.

<Español>
consigna:
Dada una lista (tambien podría ser un array) que contiene sólo números en el rango de 1 al tamaño de la lista (len(a))
busque el primer número duplicado para el cual la segunda ocurrencia tiene el índice mínimo.
En otras palabras, si hay más de 1 número duplicado, devuelva el número para el cual la segunda ocurrencia tiene un índice menor que la segunda ocurrencia del
otro número. Si no hay tales elementos, devuelva -1.

La idea principal de este algoritmo es optimizar recursos (pues se puede realizar el mismo procedimiento de una forma mas "voraz")
sabiendo que el maximo valor que puede tener cualquier elemento de la lista es el largo de la lista. Este dato es muy importante
ya que permite indexar la lista con sus propios valores.

Por ende la aproximacion es la siguiente:
Dada una lista en la que puedo tener solamente valores que van desde 1 hasta len(list) [largo de lista], lo que se ira haciendo es
marcar los indices que representan esa lista , marcandolos de manera negativa. De esta manera si existe un 3 , el valor que lo representa
en la lista es el de indice 2 (recordemos que las listas comienzan en cero). Se realiza esta marcación sucesivamente hasta encontrar un valor negativo...
En ese caso resolvimos la incognita. :-D

Proceso:
evaluar cada elemento de la lista, si es negativo es el numero "marcado" (el que buscamos y que previamente marcamos)
si no lo es marcar su correspondiente posición en la lista.

dado el array/lista = [4,1,4,3,2,1] a simple vista 4 es la respuesta..

el algoritmo evaluara el primer valor: 4.
- ¿es negativo? (dado que es el primer caso... es un poco ingenua la pregunta pero mas adelante tendra sentido)
- No, es positivo , entonces la posicion 0 (que es el indice - 1) sera marcado como negativo.
- pero , ¿si lo marco negativo? afectara a las iteraciones posteriores.
- No, porque siempre buscamos el valor absoluto , no el valor puntual, a pesar de trabajar con enteros.

1° iteración
item = 4 (el primero)
a = [4,1,4,-3,2,1] Se marco el elemento cuyo indice es 4-1... 3.

2° iteración
item = 1 (el segundo)
a = [-4,1,4,-3,2,1] Se marco el elemento  cuyo indice es 1-1...0

3° iteración
item = 4 (el tercero)
la función evaluara si es positivo a[4-1] = a[3] = -4 , Es negativo entonces... ¡Bingo! El "marcado".

en este caso la función devuelve -4 * -1 (porque el foco está en el índice)
pero en su lugar se puedes usar  tranquilamente el retorno de la función fabs o simplemente el ítem...
el resultado será 4 (en este caso), el que estamos buscando.

"""

def firstDuplicate(a):
    from math import fabs
    for item in a:
        if a[int(fabs(item))-1] < 0:
            return(int(fabs(item)))
        else:
            a[int(fabs(item))-1] *= -1
    return -1



def test():
    print("1: "+ str(firstDuplicate([2, 3, 3, 1, 5, 2])))
    print("2: "+ str(firstDuplicate([2, 4, 3, 5, 1])))
    print("3: "+ str(firstDuplicate([1])))
    print("4: "+ str(firstDuplicate([2, 2])))
    print("5: "+ str(firstDuplicate([2, 1])))
    print("6: "+ str(firstDuplicate([2, 1, 3])))
    print("7: "+ str(firstDuplicate([2, 3, 3])))
    print("8: "+ str(firstDuplicate([2, 3, 3])))
    print("9: "+ str(firstDuplicate([3, 3, 3])))
    print("10: "+ str(firstDuplicate([8, 4, 6, 2, 6, 4, 7, 9, 5, 8])))
    print("11: "+ str(firstDuplicate([10, 6, 8, 4, 9, 1, 7, 2, 5, 3])))



test()
