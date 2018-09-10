#En un While siempre debe inicializar con un contador y luego se
#el loop de salida

i = 1
while i < 4:
    print('\nOuter Loop Iteration:',i)
    i+=1

    j = 1
    while j < 4:
        print('\tInner Loop Iteration:',j)
        j+=1
