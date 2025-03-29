salario_inicial = float(input("Digite o salário inicial: R$"))
aumento_percentual = float(input("Digite o aumento percentual inicial (em %): "))
anos = int(input("Digite o número de anos: "))

salario_atual = salario_inicial

for ano in range(1, anos + 1):
    aumento = salario_atual * (aumento_percentual / 100)
    salario_atual += aumento
    aumento_percentual *= 2  # O aumento percentual dobra a cada ano

print(f"O salário atual após {anos} anos é: R${salario_atual:.2f}")