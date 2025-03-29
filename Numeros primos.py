contador = 0
numero = 2
primos = []

while contador < 100:
    divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
    if divisores == 2:
        primos.append(numero)
        contador += 1
    numero += 1

for primo in primos:
    print(primo)
