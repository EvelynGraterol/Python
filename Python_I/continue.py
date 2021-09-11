#if i==2 and j==1:
       #break
        #print('Break inner loop at i=2 j=1')

for i in range(1,4): #Tomo  un valor y evaluo todo y asi sucesivaente
    for j in range (1,4):
        if i==1 and j==1:
            print('Continues inner loop t i=1 j=1')
            continue # Si el condicional de if determina que es cierto
                    #El continue es usado para omitir una operacion simplee
                    #de un loop y pasar a la siguiente
        if i==2 and j==1:
            print('Breaks inner loop at i=2 j=1')
            break   #rompe el ciclo en este grupo
        print('Running i=',i,'j=',j)
                    
#NOTA IMPORTANTE: La identacion es super importante dentro de un bucle
#ASI COMO la distancia entre cada linea de codigo a ser leida WOW!!!!
