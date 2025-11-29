frase=str(input("Dime una frase: "))
palabras_separadas=frase.split(" ")
cantidad_de_palabras=len(palabras_separadas)

tiempo=(cantidad_de_palabras / 2)

if tiempo>60:
    print("Para flaco tampoco te pedi testamento")
else:
    print("Dijiste",cantidad_de_palabras,"y tardaste",(cantidad_de_palabras / 2),"segundos")
print("Dalto lo diria en",cantidad_de_palabras*100//2*1.3/100,"segundos")