idade = int(input("Digite a idade do nadador: "))

if idade>5 and idade<7:
    print("Categoria infantil A")
elif idade>8 and idade<11:
    print("Categoria infantil B")
elif idade>12 and idade<30:
    print("Categoria juvenil A")
elif idade>14 and idade<17:
    print("Categoria juvenil B")
elif idade<5:
    print("Idade insuficiente")
else:
    print("Maiores de 18 anos")