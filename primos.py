num1 = int(input("Intervalo 1: "))
num2 = int(input("Intervalo 2: "))


for i in range(num1,num2+1):
    primo = True
    raiz = int(i ** 0.5)
    for j in range(2,raiz+1):
        if(i % j == 0):
            primo = False
    if primo:
        print(str(i))