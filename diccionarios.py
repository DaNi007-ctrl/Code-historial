#creando diccionarios con dict
diccionario=dict(nombre="Dani",apellido="Busuioc")

#las listas no pueden ser claves porque son mutables y usamos frozenset para meter conjuntos
diccionario={frozenset(["Dani","Busuioc"]):"jajajaj"}

#creando diccionarios con fromkeys, valor por defecto, none
diccionario=dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fromkeys, cambiando el valor por defecto a "blabla"
diccionario=dict.fromkeys(["nombre","apellido"],"blabla")

print(diccionario)
