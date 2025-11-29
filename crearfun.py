#creando una funcion simple
def saludar():
    print("Hola Dani")

#ejecutando
saludar()
saludar()
saludar()
saludar()

#creando funciones que tienen parametros
def saludar(nombre,sexo):
    sexo=sexo.lower()
    if(sexo=="mujer"):
       adjetivo="maestra"
    elif(sexo=="hombre"):
       adjetivo="maestro"
    else:
       adjetivo="persona"
    print("Hola", nombre, "eres un", adjetivo)
saludar("Camila","mujer")
saludar("Dani","hombre")

def multa(fecha,via,velocidad):
   via=via.lower()
   if velocidad > 120 and via=="autopista":
      print("El dia ",fecha,"en la via", via," ha cometido una infraccion por ir demasiado rapido")
   elif velocidad < 80 and via=="autopista":
      print("El dia ",fecha,"en la via", via," ha cometido una infraccion por ir demasiado lento")
   else:
      print("Ninguna infraccion detectada")
multa("20.1.25","autopista",85)
multa("22.4.25","autopista",130)