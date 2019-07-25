#l, r = eval(dir()[0])
def comfortableNumbers(l, r):
  pairs = []
  sd = lambda valor : sum([int(x) for x in str(valor) ])
  c = lambda x,y : ( x >= y-sd(y) and x <= y+sd(y)) and  (y >= x-sd(x) and y <= x+sd(x) )
  seg =  range(l,r+1)
  while seg:
      x, *seg = seg
      pairs += [(x,i) for i in seg if c(x,i)]
  return len(pairs)

print(comfortableNumbers(10,12))