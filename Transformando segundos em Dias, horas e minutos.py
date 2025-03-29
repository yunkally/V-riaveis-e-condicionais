segundos = int(input("Digite o número de segundos: "))

dias = 0
horas = 0
minutos = 0


if segundos >= 86400:  
    dias = segundos // 86400  
    segundos = segundos % 86400  

if segundos >= 3600:  
    horas = segundos // 3600  
    segundos = segundos % 3600  

if segundos >= 60: 
    minutos = segundos // 60  
    segundos = segundos % 60  

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")
