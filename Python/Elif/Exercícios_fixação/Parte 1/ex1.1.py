n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
media = (n1 + n2)/2

if media>7:
    print(f"\nMédia = {media}\nAprovado")
elif media<5:
    print(f"\nMédia = {media}\nReprovado")
else:
    print(f"\nMédia = {media}\nRecuperação")