valor = float(input("Digite o valor de sua compra: "))
prestacao = int(input("Digite o número de prestações: "))
parcela = valor/prestacao

print(f"Valor das prestações sem juros: R$ {parcela}")