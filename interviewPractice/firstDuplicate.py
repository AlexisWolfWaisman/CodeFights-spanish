def firstDuplicate(a):
    from math import fabs
    for item in a:
        if item > 0:
            a[item-1] = -a[item-1]
        if item < 0:
            return -item
    return -1



    # from math import fabs
    # rsta = -1
    # for item in a:
    #     centinel = a[int(fabs(item))-1]
    #     if centinel > 0:
    #         a[int(fabs(item))-1] *= -1
    #     else:
    #         print()
    #         rsta = centinel * -1
    #         break
    # return rsta












        




    # minimo = len(a)
    # aux = []
    # flag = True
    # for indice in range (len(a)):
    #     if a[indice] not in aux:
    #         aux.append(a[indice])
    #     else:
    #         flag = False
    #         if indice < minimo:
    #             minimo = indice
    # if flag:
    #     return -1
    # else:
    #     return a[minimo]



"""
    Falla en el caso de que tengamos tres valores repetidos en distintos lugares
"""
    # if duplicados == []:
    #     return -1
    # try:
    #     for myIndex in range(len(duplicados)):
    #         if duplicados[myIndex] == duplicados[myIndex+1]:
    #             return duplicados[myIndex]
    # except Exception:
    #     print("fallo en:")
    #     print(duplicados)
    #     print("indice: " + str(myIndex) )









"""
    falla en la performance
"""

    # lista_duplicados = [(x,i) for i, x in enumerate(a) if a.count(x) > 1]
    # if lista_duplicados != []:
    #     dictionary = dict(lista_duplicados)
    #     invertedDictionary = {value: key for key, value in dictionary.items()}
    #     return(invertedDictionary[min(invertedDictionary.keys())])
    # else:
    #     return -1

"""
    falla en la performance
"""
# lista_rellenar = []
#     for elem in a:
#         if elem not in lista_rellenar:
#             lista_rellenar.append(elem)
#         else:
#             return elem
#     return -1

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
# print(firstDuplicate([2, 3, 3, 1, 5, 2]))