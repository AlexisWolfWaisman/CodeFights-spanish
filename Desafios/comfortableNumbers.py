#l, r = eval(dir()[0])
def comfortableNumbers(l, r):
  pairs = []
  sd = lambda valor : sum([int(x) for x in str(valor) ])
  b = lambda e : (e-sd(e),e,e+sd(e) )
  c = lambda l1,l2 : ( l1[1] >= l2[0] and l1[1] <= l2[2]) and  (l2[1] >= l1[0] and l2[1] <= l1[2])
  seg =  range(l,r+1)
  h = [b(x) for x in seg]
  while h:
      x, *h = h
      pairs += [(x[1],i[1]) for i in h if c(x,i)]
  return len(pairs)

print(comfortableNumbers(10,12))