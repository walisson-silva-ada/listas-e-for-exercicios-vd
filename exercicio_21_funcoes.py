def cadastraCliente():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    email = input("Digite o email do cliente: ")
    return [nome, cpf, email]

def comando():
    print()
    print("Escolha uma opção")
    print("0 - Sair do programa")
    print("1 - Cadastro de cliente")
    print("2 - Procurar cliente")
    print("3 - Mostrar todos clientes")
    comando = int(input())
    return comando

def mostraClientes(lista):
    print("Lista de clientes")
    for cliente in lista:
        print(cliente)
        
def procuraCliente(lista, cpf):
    for cliente in lista:
        if cliente[1] == cpf:
            return cliente
    print("Cliente não encontrado")
    
lista_clientes = []
opc = comando()
while opc != 0:
    if opc == 1:
        lista_clientes.append(cadastraCliente())
        print("Cliente cadastrado com sucesso!")
    elif opc == 2:
        cpf = input("Qual o CPF do cliente? ")
        cliente = procuraCliente(lista_clientes, cpf)
        if cliente != None:
            print("Informações do cliente: ")
            print(cliente)
    elif opc == 3:
        mostraClientes(lista_clientes)
    else:
        print("Opção inválida.")

    opc = comando() 
