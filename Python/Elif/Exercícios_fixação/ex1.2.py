t1 = int(input("Digite os gols do primeiro time: "))
t2 = int(input("Digite os gols do segundo time: "))

if t1 == t2:
    print("Houve empate!")
elif t1 > t2:
    print("O primeiro time venceu!")
else:
    print("O segundo time venceu!")