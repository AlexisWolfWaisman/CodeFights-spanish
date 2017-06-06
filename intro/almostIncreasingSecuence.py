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



