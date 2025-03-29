numero = int(input("Digite um número inteiro maior que 1: "))

if numero > 1:
    divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
    
    if divisores == 2:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")
else:
    print("Por favor, digite um número maior que 1.")
