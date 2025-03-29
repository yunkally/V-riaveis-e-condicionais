numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

soma_ponderada = 0
soma_pesos = 0

peso1 = 1
peso2 = 2
peso3 = 2

if numero1 != 0:
    soma_ponderada += numero1 * peso1
    soma_pesos += peso1

if numero2 != 0:
    soma_ponderada += numero2 * peso2
    soma_pesos += peso2

if numero3 != 0:
    soma_ponderada += numero3 * peso3
    soma_pesos += peso3

if soma_pesos > 0:
    media_ponderada = soma_ponderada / soma_pesos
    print(f"A média ponderada dos números é: {media_ponderada}")
else:
    print("Nenhum número válido foi inserido.")
