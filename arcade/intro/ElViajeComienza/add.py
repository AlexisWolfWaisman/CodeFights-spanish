"""
Traduccion del problema: Suma

Traducccion del enunciado:
    Escribir una funcion que sume dos numeros.


Enfoque (approach):
    para realizar la suma de manera optimizada se usa la biblioteca math
    por otro lado basta con usar el operador correspondiente para hacerlo de manera "pure python"
"""
def add(param1, param2):
    from math import fsum
    return(fsum([param1,param2]))

def test():
    print(add(1,2))
    print(add(0,1000))

test()
