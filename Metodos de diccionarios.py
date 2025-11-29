diccionario = {
    "nombre":"Dani",
    "apellido" : "Busuioc",
    "años":16
}

#nos sirve para iterar
claves= diccionario.keys()
print(claves)

#nos muestra el valor de las llaves
claves1= diccionario.get("nombre")#la diferencia entre poner get y no ponerlo es que con get no se termina el programa
print(claves1)

#elimina todo el diccinario(el contenido)
#claves2=diccionario.clear()

#elimina un elemento del diccionario
diccionario.pop("nombre")
print(diccionario)

#obtenemos un elemnto dict_item iterable
claves3=diccionario.item()
print(claves3)