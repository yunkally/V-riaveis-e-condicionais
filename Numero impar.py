numero = int(input("Digite um número ímpar: "))

if numero % 2 != 0:
    numero_anterior = numero - 2
    numero_proximo = numero + 2

    quadrado_anterior = numero_anterior ** 2
    quadrado_proximo = numero_proximo ** 2

    diferenca = quadrado_proximo - quadrado_anterior

    print(f"A diferença entre o quadrado do número anterior ({quadrado_anterior}) e do próximo número ímpar ({quadrado_proximo}) é: {diferenca}")
else:
    print("Por favor, digite um número ímpar.")
