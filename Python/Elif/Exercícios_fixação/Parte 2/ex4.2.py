n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

op = input("Operações matemáticas - Digite:\n\n* para multiplicação\n/ para divisão\n+ para soma\n- para subtração\n\n")

if op == "*":
    print(f"Resultado da multiplicação = {n1*n2}")
elif op == "/":
    print(f"Resultado da divisão = {n1/n2}")
elif op == "+":
    print(f"Resultado da soma = {n1+n2}")
elif op == "-":
    print(f"Resultado da subtração = {n1-n2}")