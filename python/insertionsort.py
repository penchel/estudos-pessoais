numeros = [42, 7, 15, 29, 3, 18, 11, 90, 25, 8, 37, 54, 2, 13, 70]

for j in range(1, len(numeros)):
    x = j-1
    
    while(numeros[j] < numeros[x] and j >= 0):
        x-=1

    temp = numeros[j]

    for k in range(j,x,-1):
        numeros[k] = numeros[k-1]

    numeros[x+1] = temp



print(numeros)