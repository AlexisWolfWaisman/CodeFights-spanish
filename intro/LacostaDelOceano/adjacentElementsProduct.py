"""
Traduccion del problema: Producto de elementos adyacentes

Traducccion del enunciado:
    Dado un arreglo de enteros, encontrar el par de elementos adyacentes que tenga el producto mas grande
    devolver ese producto
Enfoque (approach):
    1) Tomamos de a dos elementos desde el primer elemento del array (lista ,en realidad, en este caso)
    2) los introducimos a una lista llamada products
    3) elegimos el maximo elemento
"""
def adjacentElementsProduct(inputArray):
    products = []
    for i in range(len(inputArray)-1):
        product = inputArray[i] * inputArray[i+1]
        products.append(product)
    return(max(products))

def test():
    print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))
    print(adjacentElementsProduct([-1, -2]))

test()



