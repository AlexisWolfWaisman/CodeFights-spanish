"""
Traduccion del problema: comprobar Palindromo

Traducccion del enunciado:
    dada una cadena verificar si es una palíndromo
    Palíndromo:  "[...]es una palabra, número o frase que se lee igual adelante que atrás[...]" <<wikipedia>>
Enfoque (approach):
    Tomamos la cadena, la revertimos y comprobamos si es la misma.
"""
def checkPalindrome(inputString):
    return (inputString == inputString[::-1])
def test():
    print(checkPalindrome("aabaa"))
    print(checkPalindrome("abac"))
test()