p = float(0)

v = float(input("Digite o valor: "))
t = float(input("Digite a taxa: "))
temp = int(input("Digite o tempo: "))

p = (v + (v * (t/100) * temp))

print(f"O valor da prestação é: {p}")

input("Digite enter para sair")