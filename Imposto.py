valor_total = float(input("Digite o valor total das mercadorias compradas (R$): "))

imposto = 0

if valor_total > 500:
    excedente = valor_total - 500
    imposto = excedente * 0.50
else:
    imposto = 0

print(f"O valor do imposto a ser pago é: R${imposto:.2f}")
