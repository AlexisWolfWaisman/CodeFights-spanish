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
