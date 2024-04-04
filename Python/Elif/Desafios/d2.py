v = float(input("Digite a velocidade do carro: "))

if v>80:
    multa = (v-80)*7
    print(f"Você foi multado!\nValor da multa = R$ {multa}")