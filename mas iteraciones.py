frutas=("Manzana","Banana","Naranja","Ciruela")
cadena="Hola Dani"
numeros=[2,6,8,10]
#evitando que se coma una banana
for fruta in frutas:
    if fruta == "Banana":
        continue
    print("Me voy a comer una",fruta)

#evitar que el bucle siga ejecutandose(el else nos e ejecuta tampoco)
for fruta in frutas:
    print("Me voy a comer una",fruta)
    if fruta== "Naranja":
        break
else:
    print("bucle terminado")
        
#recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
#for en una sola linea de texto
numeros_duplicados=[x*2 for x in numeros]
print(numeros_duplicados)