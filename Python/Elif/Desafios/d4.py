d = int(input("Digite a distância em km: "))

if d<=200:
    valor = d*0.5
    print(f"Valor da passagem R$ {valor}")
else:
    valor = d*0.45
    print(f"Valor da passagem R$ {valor}")