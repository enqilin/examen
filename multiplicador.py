numero_magico=12345679
numero_usuario=int(input("Numero de carateres entre [1,9]"))
if not 1<numero_usuario <9:
  numero_usuario=int(input("Numero de carateres entre [1,9]"))
numero_usuario*9
numero=numero_magico*numero_usuario
print(numero)