diccionario={
    "nombre":"Daniel",
    "apellido":"Busuioc",
    "edad":16
}

#recorriendo el diccionario para obtener la clave
for key in diccionario:
    key
    print("La clave es",key)
    
#recorriendo el diccionario con items( ) para obtener la clave y el valor
for datos in diccionario.items():
    key=datos[0]
    value=datos[1]
    print("En la clave",key,"el valor es",value)