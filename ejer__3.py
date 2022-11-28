def funcion_triangulo(n,char):
  for x in range(1,n+1):   
    for y in range(1,n+1):
       if y<=x:
          print(char," ", end='')
       else:
          print("  ", end='')
    print()

n=-1
while n<0:
  n=int(input("Ingresa valor de N:> "))

  char=input("Ingresa un caracter:> ")

funcion_triangulo(n,char)
