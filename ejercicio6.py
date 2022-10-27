lista=[3,56,87,42,65,29,29]

def modificar():
  for numero in lista:
  lista1=sorted(lista)
  if not numero%2==0:
    lista.remove(numero)
  else:
    numero+=numero
    lista.insert(0,numero)
  return lista
lista[0]==sum(lista[1:])