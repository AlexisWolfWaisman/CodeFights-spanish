"""
Traduccion del problema: Siglo dependiendo del año

Traducccion del enunciado:
    Dado un año determinado devolver su canturia (siglo).
    La primer centuria pasa desde el año 1 al año 100,
    La segunda desde el año 101 hasta incluirlo al año 200
    y así sucesivamente.

Enfoque (approach):
    1) dividimos el año por 100 (un siglo) ej. : 1901 / 100 = 19.01
    2) usamos la funcion ceill (si el valor es un poco mayor al entero retorna el entero mayor mas proximo)

"""
def centuryFromYear(year):
    from math import ceil
    return ceil(year/100)

def test():
    print(centuryFromYear(1905))
    print(centuryFromYear(1988))
    print(centuryFromYear(1700))

test()
