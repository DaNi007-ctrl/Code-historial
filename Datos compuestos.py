#creando una lista (se puede modificar)
lista = ["Daniel",40.5,True]

#creando una tupla (no se puede modificar)
tupla = ("Daniel",40.5,True)

#para mostrar una posicion de la matriz
print(lista[1])
print(tupla[1])

#esto es valido
lista[2] = "Busuioc"

#esto no es valido
#tupla[2] = "Busuioc"
#print(tupla[2])

#creando un conjunto (set), (no se puede llamar a los elmentos por su indice, no almacena datos duplicados)
conjunto = {"Daniel",40.5,True,True}
print(conjunto)

#creando un diccionario (dict), (separamos con comas)
diccionario = {
    "nombre": "Daniel",
    "pulgadas" : 40.5,
    "estado" : True,
    "dato duplicado" : True
    #key : value
}

print(diccionario["nombre"])
print(diccionario["pulgadas"] + 2)