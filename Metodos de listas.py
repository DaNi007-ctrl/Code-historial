#creando una lista con list
lista=list(["Hola","Dani",16])
print(lista)

#devuelve la cantidad de elementos de la lista
cadena="Hola"
resultado=len(lista)
print(resultado)

#añade un elemento a la lista
lista.append("Tung")
print(lista)

#añade un elemento a la lista en un indice especifico
lista.insert(0,"Blabla")
print(lista)

#añade varios elementos a la lista
lista.extend([22,35,12])
print(lista)

#eliminando un elemento de la lista por su indice(si pongo un -1, se elmina el ultimo elemnto de la lista)
lista.pop(0)
print(lista)

#remueve un elemento por su valor
lista.remove("Hola")
print(lista)

#elimina todo
#lista.clear()

#te ordena los valores de la lista(solo acepta numeros y trues y falses)
lista.sort(lista) #si pongo reverse=True le da la vuelta

#invirtiendo los elementos de una lista
lista.reverse()
print(lista)