var_1 = "Módulo 1 de Python "
var=var_1.lower
longitud=len(var_1)
division=longitud/7
print(round(division,4))
def funcion1():
  funcion=12-(4*2)-(2+2)
  return funcion
def funcion2():
  funcion= 12-4*(2-2)+2
  return funcion
def funcion3():
  edad=int(input("Introduce la edad que tienes:  " ))
  if edad<18:
    print("Menor de edad")
  else:
    print("Mayor de edad")
    