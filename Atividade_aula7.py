pares=[]
impares=[]

print('Digite 20 números pares:')
for _ in range(20):
    while true:
        numero = int(input(f"numero par {len(pares) + 1}:"))
        if numero % 2 == 0:
            pares.append(numero)
            break
        else:
            print('Esse número não é par. Tente novamente.')

print('Digite 20 nnúmeros ímpares:')
for _ in range(20):
    while true:
        numero = int(input(f'numero ímpar {len(impares) + 1}:'))
        if numero % 2!= 0:
        impares.append(numero)
        break
    else:
        print('Esse número não é ímpar. Tente novamente.')

print('números pares:', pares)
print('números impares', impares)