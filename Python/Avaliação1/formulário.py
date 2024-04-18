from validacoes import validaNome, validaCpf, validaTel, validaEmail, validaCep


print("-------------------------- ANÁLISE DE CRÉDITO ------------------------")
print("\nPreencha o formulário para a solicitação da análise:\n")

nome = input("Nome completo: ")
cpf = input("CPF: ")
tel = input("Telefone/celular: ")
email = input("E-mail: ")
cep = input("CEP: ")
endereco = input("Endereço: ")
sal = float(input("Salário líquido: "))
val = float(input("Valor do empréstimo: "))
meses = int(input("Quantidade de parcelas: "))

print("\n\n")

if((validaNome(nome)==False) or (validaCpf(cpf)==False) or (validaTel(tel)==False) or (validaEmail(email)==False) or (validaCep(cep)==False)):

    print("Erros encontrados: \n")

    if validaNome(nome) == False:
        print("Nome incompleto")

    if validaCpf(cpf) == False:
        print("CPF Inválido")

    if validaTel(tel) == False:
        print("Telefone Inválido")
    
    if validaEmail(email) == False:
        print("E-mail inválido")

    if validaCep(cep) == False:
        print("Cep inválido")

    print("\nPreencha campos novamente!")

else:
    prestacao = val/meses

    if (prestacao > sal):
        print("Solicitação de crédito NEGADA! As prestações excedem o salário do solicitante.")

    else:
        print(f"Solicitação de crédito APROVADA! O valor de cada prestação equivale a R$ {prestacao}")