x = int(input("Ingrese un numero a comparar mediante el uso del while: "))

while x < 10:
    if x>7:
        x+=2
        continue
    x = x+1
    print("Todavia esta dentro del ciclo")
    if x == 8:
        break
print ("Valor fuera del ciclo")

   
