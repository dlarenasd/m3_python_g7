edad = 27
#Juan es mayor de edad?
print(edad>=18)#True
print (edad<18)#False

#Juan se graduó antes de los 18 años?
edad_graduacion_colegio = 17
print(edad_graduacion_colegio <18)#True
print(edad_graduacion_colegio >18) #False
print(edad_graduacion_colegio ==18) #False
print(edad_graduacion_colegio >=18) #False

#Juan NO tiene 4 años de experiencia laboral?
experiencia_laboral = 4
print(experiencia_laboral != 4) #False
print(experiencia_laboral == 4) #True
print(experiencia_laboral < 4) #False
print(experiencia_laboral > 4) #False
print(experiencia_laboral <= 4) #True
print(experiencia_laboral >= 4) #True
print(experiencia_laboral < 4 or experiencia_laboral > 4) #False

#Juan tiene hijos?
numero_hijos = 0
print (numero_hijos > 0) #False
print (numero_hijos < 1) #True
print (numero_hijos == 0) #True
print (numero_hijos != 0) #False

#Juan egresó ya habiendo cumplido 22 años?
anios_universidad = 6
edad_egreso_universidad = (edad_graduacion_colegio + anios_universidad)
print(edad_egreso_universidad >=22) #True

nombre ="Juan"
me_llamo_juan = nombre == "Juan" #--> se le asigna a me_llamo_juan el RESULTADO de la comparación entre nombre y Juan, en este caso True