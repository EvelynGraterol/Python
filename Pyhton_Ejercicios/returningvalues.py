#Returning values

#Estudio de la funcion: str(), la cual retorna una reprsentacion string del
#valor especifico cuando su argumento sea llamado.Tambien puede retornar un valor
#cuando sea llamado mediante la funcion return

#Funciones de estudio: str() y return



num = input('Enter An Interger:') #Recuerda que este dato es str y deber ser pasado a interger o float
def square(num):
    if not num.isdigit(): #Es un Metodo para validar la cadena de entrada (isdigt), devuelve true si la cadena es numerica, de lo contrario es false.
         return'Invalid Entry'
    num = int(num)
    return num*num  #Cuando una funcion haga retorno de datos,estos pueden
                    #ser asignados a una variable
                    #El comando de retorno de python especifica que valor se devolvera
                    #cuando se llama una funcion.

print(num,'Squared is:',square(num))
