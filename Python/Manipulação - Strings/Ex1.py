frase = (input("Digite a frase: "))

c1 = frase[4]
c2 = frase[2:4] #2 até o 4
c3 = frase[:4] #do inicio até posição 4
c4 = frase[4:] #da posição 4 até o fim
c5 = frase[2:8:2] #2 até 8 pulando de 2 em 2
c6 = len(frase) #quant de carac que tem dentro da string
c7 = frase.count("o") #conta quantos "o" tem
c8 = frase.find("cotil") #procura se tem a palavra e exibe a posição que inicia a escrita, caso não tenha exibe -1
c9 = "cotil" in frase #procura dentro da frase e retorna true or false
c10 = frase.upper() #deixa maiúsculas as letras
c11 = frase.lower() #letras minúsculas
c12 = frase.capitalize() #primeira maiúscula
c13 = frase.title() #primeira letra de cada palavra maíscula
c14 = frase.replace("Javascript", "Python") #troca palavra

print(f"A quarta posição é: {c1}")
print(f"Posição 2 até 4: {c2}")
print(f"Inicio até a posição 4: {c3}")
print(f"Posição 4 até o fim: {c4}")
print(f"Posição 2 até 8 pulando de 2 em 2: {c5}")
print(f"Quantidade de caracteres que a frase possui: {c6}")
print(f"Quantidade de 'o' presente: {c7}")
print(f"posição da palavra 'cotil' na frase: {c8}")
print(f"Existe a palavra 'cotil' na frase: {c9}")
print(f"Frase maiúscula: {c10}")
print(f"Frase minúscula: {c11}")
print(f"Primeira maíscula: {c12}")
print(f"Título: {c13}")
print(f"Troca palavra: {c14}")

'''Comentários'''