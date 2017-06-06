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
def shapeArea(n):
    return (n**2 + (n-1)**2)
print(shapeArea(5))
