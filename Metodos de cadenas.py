cadena1="Soy, dani"
cadena2="Bienvenido Lucas"
resultado= cadena1.upper
print(resultado)
#dir: nos muestra todo lo que podemos hacer con esas variable
resultado= dir(cadena1)

#upper: te convierte todo a mayusculas
resultado1= cadena1.upper()

#lower: te convierte todo a minusculas
resultado2= cadena1.lower()

#capitalize: convierte solo la primera letra a mayusculas
resultado3= cadena1.capitalize()

#find: buscamos una cadena en otra cadena, si no hay coincidencias nos devuelve -1
resultado4= cadena1.find("i")

#index: buscamos una cadena en otra cadena, si no hay coincidencias nos devuelve una excepción
resultado5= cadena1.index("i")

#isnumeric: si es numerico devuelve true, aunque sea sting, si hay numero dentro pone ture
resultado6= cadena1.isnumeric()

#isalpha: si es alfanumerico nos devuelve true, solo acepta de la A a la Z (los espacios no valen(hay que quitarlos)) 
resultado7= cadena1.isalpha()

#count: buscamos una cadena en otra cadena,nos dice cuantas veces se repite
resultado8= cadena1.count("i")

#len: contamos cuantos caracteres hay en la cadena
resultado9= len(cadena1)

#startswith: verificamos si una cadena empieza con otra dada, si es asi devuelve true
resultado10= cadena1.startswith("S")

#endswith: verificamos si una cadena termina con otra dada, si es asi devuelve true
resultado11= cadena1.endswith("i")

#replace: remplaza un pedazo de una cadena dada, por otra dada
resultado12= cadena1.replace("Soy","Eres")

#split: nos separa cadenas con otras que le pasamos
resultado13= cadena1.split("y")

print(resultado9)
