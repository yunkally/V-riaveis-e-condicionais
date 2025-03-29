numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

soma = 0
quantidade = 0

if numero1 != 0:
    soma += numero1
    quantidade += 1

if numero2 != 0:
    soma += numero2
    quantidade += 1


if numero3 != 0:
    soma += numero3
    quantidade += 1


if quantidade > 0:
    media = soma / quantidade
    print(f"A média dos números é: {media}")
else:
    print("Nenhum número válido foi inserido.")
