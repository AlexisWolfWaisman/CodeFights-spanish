#l, r = eval(dir()[0])
def comfortableNumbers(l, r):
  parejas = []
  sumardigitos = lambda valor : sum([int(x) for x in str(valor) ])
  busqueda = lambda e : [x for x in range( e - sumardigitos(e), e+1+sumardigitos(e) ) ]
  segmento =  range(l,r+1)
  for primElem in segmento:
    afinidadPrimElem = busqueda(primElem)
    for segElem in afinidadPrimElem:
      comun = set(afinidadPrimElem).intersection(set(busqueda(segElem)))
      comun = comun.intersection(set(segmento))
      par = [primElem,segElem]
      if (primElem in comun and segElem in comun and sorted(par) not in parejas and primElem != segElem):
        parejas.append(sorted(par))
  print(len(parejas))
  return len(parejas)

print(comfortableNumbers(1,1000))