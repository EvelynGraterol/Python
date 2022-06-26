def divisors(num):
    divisors = []
    for i in range(1 , num+1):
        if num % i == 1:
            divisors.append(i)

def run():
    num = int(input("Ingrese el valor: "))
    print(divisors(num))

if __name__ == '__main()__':
    run()