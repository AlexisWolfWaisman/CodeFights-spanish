#! usr/bin bash
# !-*- CODING:UTF-8 -*-


def stringsCrossover(a, r):
    s = 0
    while a:
        x, *a = a
        for y in a:
            print(list(r in x for r, *x in zip(r, x, y)))
            s += all(r in x for r, *x in zip(r, x, y))

    return s



def test():
    inputArray =  ["abc",
 "aaa",
 "aba",
 "bab"]
    result = "bbb"
    print(stringsCrossover(inputArray, result))


test()