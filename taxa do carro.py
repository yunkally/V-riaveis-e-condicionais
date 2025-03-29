dias = int(input("Digite o número de dias que o carro foi alugado: "))
km_rodados = float(input("Digite a quantidade de quilômetros rodados: "))

custo_diario = 90
taxa_extra = 12
km_limite = 100

valor_total = dias * custo_diario

if km_rodados > km_limite:
    km_excedente = km_rodados - km_limite
    valor_total += km_excedente * taxa_extra

print(f"O valor total a ser pago é: R${valor_total:.2f}")
