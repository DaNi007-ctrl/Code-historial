numeros=[4,7,1,42,15]

#encontrando el numero mayor de una lista
numero_mas_alto=max(numeros)
print("El numero mas alto es: ", numero_mas_alto)

#encontrando el numero menor de una lista
numero_mas_bajo=min(numeros)
print("El numero mas bajo es: ", numero_mas_bajo)

#redondeando a 6 decimales
numero=round(12.345678,2)
print(numero)

#retorna false en caso de que le pasemos un 0,vacio,false,ninguno
resultado_bool=bool(0)
print(resultado_bool)

#retorna true si todos los valores son verdaderos
resultado_all=all([1,2,3])
print(resultado_all)

#suma todos los valores de un iterable
resultado_sum=sum(numeros)
print(resultado_sum)