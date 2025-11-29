animales={"gato","perro","loro","cocodrilo"}
numeros={1,2,3,4}

#recorrieno animales
for animal in animales:
    print("Ahora el animal es",animal)
    
#recorrinedo numeros
for numero in numeros:
    print("Ahora el numero es",numero)
    print(numero*10)
    
#iterando dos listas a la vez con el mismo numero de elementos
for numero,animal in zip(animales,numeros):
    print("Recorriendo lista 1:",numero)
    print("Recorriendo lista 2:",animal)
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice=num[0]
    valor=num[1]
    print("El indice es",indice,"y el valor es",valor)
    
#usando for/else
for num in numeros:
    print("Ejecutando el bucle, valor actual",num)
else:
    print("EL bucle termino")