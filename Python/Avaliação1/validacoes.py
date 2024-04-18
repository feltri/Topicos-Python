def validaNome(nome):
    cont = nome.split()
    nome = nome.title()

    if len(cont) < 2:
        return False
    else:
        return True
    

def validaCpf(cpf):
    # Remover caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verificar se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False
    else:
        return True
    
def validaTel(tel):
    tel = ''.join(filter(str.isdigit, tel))

    if (len(tel) == 10) or (len(tel) == 11):
        return True
    else:
        return False

def validaEmail(email):
    email = email.lower()
    if((email.count("@")==1) and (email.count("gmail")==1)):
        return True
    else:
        return False

def validaCep(cep):
    cep = ''.join(filter(str.isdigit, cep))

    if (len(cep) == 8):
        return True
    else:
        return False
    