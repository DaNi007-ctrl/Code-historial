otros_cursos_min= 2.5
otros_cursos_max= 7
otros_cursos_promedio= 4
dalto_curso= 1.5

crudo_dalto=3.5
crudo_promedio=5

dif_min=100-((dalto_curso*100)/otros_cursos_min)
dif_max=100-((dalto_curso*1000)//otros_cursos_max)/10
dif_promedio=100-((dalto_curso*100)/otros_cursos_promedio)

dif_crudo_dalto=round(100-((dalto_curso*100)/crudo_dalto))
dif_crudo_promedio=round(100-((otros_cursos_promedio*1000)/crudo_promedio)/10)

r1= round((((otros_cursos_promedio*100)/dalto_curso))/10)
r2=round(((dalto_curso*100)/otros_cursos_promedio))/10

print("La diferencia de porcentage con el curso minimo es de ",dif_min," %")
print("La diferencia de porcentage con el curso maximo es de ",dif_max," %")
print("La diferencia de porcentage con el curso promedio es de ",dif_promedio," %")
print("-------------------------------------------")
print("El tiempo vacio eliminado de Dalto es de ",dif_crudo_dalto," %")
print("El tiempo vacio eliminado del promedio es de ",dif_crudo_promedio," %")
print("-------------------------------------------")
print("Ver 10 horas de este curso equivale a ", r1, " horas de otros cursos")
print("Ver 10 horas de otros cursos equivale a ", r2, " horas de este curso")