import random

n = random.randrange(0,5)

user = input("Tente adivinhar o número: ")
if user == n:
    print("Você acertou!")
else:
    print("Você errou!")