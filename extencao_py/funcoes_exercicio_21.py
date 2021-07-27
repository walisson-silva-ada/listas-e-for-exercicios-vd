#exercicio 21

def cadastra(dicionario):
    cpf = input("Digite o CPF do usuario ") 
    nome = input("Digite o nome do usuario ") 
    email = input("Digite o email do usuario ") 
    dicionario.update({cpf : {'nome':nome,'cpf':cpf,'email':email}})
    return dicionario

def busca(dicionario, cpf):
    if dicionario.get(cpf, False) == False: 
        print("CPF não encontrado") 
        pergunta(dicionario) 
    else: 
        print(dicionario[cpf]) 
        pergunta(dicionario) 
def pergunta(dicionario): 
    print("Selecione uma das opções: ") 
    print("1 - Cadastrar clientes") 
    print("2 - Buscar um CPF") 
    print("3 - Ver users cadastrados") 
    print("0 - Sair") 
    x = input() 
    if x == '1': 
        dicionario = cadastra(dicionario)
        x = pergunta(dicionario)
    elif x == '3': 
        print(dicionario) 
        x = pergunta(dicionario) 
    elif x == '0': 
        print("------Fim-------") 
    elif x == '2': 
        cpf = input("digite o cpf que deseja buscar: ")
        busca(dicionario, cpf)
    else: 
        print("OPÇÃO INVÁLIDA") 
        pergunta(dicionario)
        

geral = {} 
pergunta(geral)