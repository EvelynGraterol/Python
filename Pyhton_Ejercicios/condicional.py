horas = int(input('Ingrese en valor de horas:'))
minutos = int(input('Ingrese el valor en minutos:'))
segundos = int(input('Ingrese el valor en segundo:'))

horas_seg = horas*3600
min_seg = minutos*60
seg = segundos
Suma = horas_seg + min_seg + seg

Total_horas = Suma//3600
resto_horas = Suma%3600
    
if  resto_horas > 60 :

     minutos = resto_horas//60

     segundos  = resto_horas%60

          
else:
     minutos = 0
     segundos = resto_horas
 
                        
print('La cantidad de horas es:',Total_horas,'h')
print('La cantidad de minutos es:',minutos,'min')
print('La cantidad de segundos es:',segundos,'seg')
#print(Total_minutos)
#print(segundos_nuevos)
#print(segundos_sobrantes)
#print(Total_segundos)

