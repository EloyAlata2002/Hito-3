lista=[1,2,3,4,5,6]
#imprimir lista
print(lista)
#agregar elemento al final de la lista
lista.append(7)
print(lista)
#mostrar un elemento de la lista
print(lista[1])
#recorrer lista
for x in lista:
  print(x)
#crear una sublista
lista2=[]
for x in lista:
  lista2.append(x)
print(lista2)
#imprimir las lista al revez 
lista3 = ["naranja", "mango", "kiwi", "piña", "platano"]
lista3.sort()
print(lista3)
#insertar una posicion 0
lista4 = ["manzana", "platano", "cereza"]
lista4.insert(0, "pera")
print(lista4)
#longitud de la lista
print(len(lista4))
#Eliminar elemento de la lista
lista4.pop(3)
print(lista4)
#encotrar elemento de una lista
if "manzana" in lista4:
  print("Si esta en la lista")
