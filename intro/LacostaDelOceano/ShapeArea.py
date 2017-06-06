"""
Traduccion del problema: Area de figura

Traducccion del enunciado:
    se define un poligono de n-bloques. La tarea a concretar es encontra el area del poligono sabiendo n.
    un polígono de 1-bloque es un simple cuadrado cuyo lado mide 1.
    Un polígono de n-bloques se obtiene a partir del poligono de n-1-bloques y anexandole un poligono de 1-bloque en cada costado.

Enfoque (approach):
    1) Aplicamos una formula matematica que resuelve nuestro problema
"""
def shapeArea(n):
    return (n**2 + (n-1)**2)

def test():
    print(shapeArea(2))
    print(shapeArea(3))

test()





"""
Otra aproximacion consiste en usar la formula incremental 2*((n-1)**2)
PD: se podría aplicar recursividad.
"""
# def shapeArea(n):
#     Qsquare = 1
#     step = 1
#     area = 0
#     while True:
#         if step == n:
#             area = 2*((n-1)**2) + Qsquare
#             break
#         step += 1
#         Qsquare = Qsquare + 2
#     return(area)