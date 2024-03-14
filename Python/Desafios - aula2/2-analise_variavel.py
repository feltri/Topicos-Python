txt = input("Digite algo: ")

print(f"\nO tipo da variável é: {type(txt)}")

print(f"É numérico? {txt.isnumeric()}")
print(f"É string? {txt.isalpha()}")
print(f"É alfanumérico? {txt.isalnum()}")
print(f"Possui letras maíusculas? {txt.isupper()}")
print(f"Possui letras minúsculas? {txt.islower()}")
print(f"Possui casas decimais? {txt.isdecimal()}")

input("\nDigite enter para fechar")