def fibonacci(x,y):
    if(x+y>num1):
        return
    else:
        print(x+y)
        fibonacci(y,x+y)

num1 = int(input("numero: "))
print(0)
if(1<=num1):
    print(1)
    print(1)
fibonacci(1,1)
