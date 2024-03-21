nome = (input("Digite o nome da sua cidade: "))

primeira = nome.split()[0]

if(primeira.lower() == "santo"):
    print("Sua cidade começa com Santo")

else:
    print("Sua cidade não começa com Santo")