#exercicio 20
from random import randint
def cria_baralho():
    c = ['A',2,3,4,5,6,7,8,9,10,'Q','J', 'K']
    p = ['A',2,3,4,5,6,7,8,9,10,'Q','J', 'K']
    o = ['A',2,3,4,5,6,7,8,9,10,'Q','J', 'K']
    e = ['A',2,3,4,5,6,7,8,9,10,'Q','J', 'K']
    return [c, p, o, e]

def puxa_carta(l):
    nipe = randint(0,3)
    carta = randint(0,12)
    if l[nipe][carta] != 0:
        if carta > 9:
            valor = 10
        else:
            valor = carta + 1
        puxada = l[nipe][carta]
        l[nipe][carta] = 0
        return [valor, puxada]
    puxa_carta(l)

def ganhador(j):
    aux = 0
    camp = ""
    for x in j:
        if x[1] > aux and x[1] <= 21:
            aux = x[1]
            camp = x[0]
    return camp
    
def placar(l):
    print("###### Placar ######")
    g = ganhador(l)
    for x in l:
        if x[0] == g:
            print("Vencedor:",x[0], "->", x[1], "pontos!!!")
        else:
            print(x[0], "->", x[1])
            
def alguem_jogando(jog):
    for x in jog:
        if x[2] == 1 and x[1] < 21:
            return True
    return False
    
            
def jogar(jog, deck):
    if alguem_jogando(jog) == True:
        for x in jog:
            if x[2] == 1 and x[1] < 21 :
                print("\n##### Vez de:", x[0].upper(), "#####")
                r = input("deseja puxar uma carta? (s/n)")
                if r.upper() == "S":
                    carta = puxa_carta(deck)
                    x[1] += int(carta[0])
                    print("carta puxada:", carta[1], "\nforam somados ", carta[0], "ponto(s). \nTotal jogador:", x[1])
                    if x[1] > 21:
                        print("##### ESTOUROU!!!! #####")
                    jogar(jog, deck)
                else:
                    print("##### PAROU! #####")
                    x[2] = 0
                    jogar(jog, deck)
    else:
        print("##### FIM DE JOGO #####")
        return placar(jog)
      
def ini():
    x = 1
    print("###### INICIO DE JOGO ######\n")
    qtde = int(input('Quantos jogadores irão participar: '))
    jog = []
    for x in range(qtde):
        nome = input('Digite o nome do jogador:')
        jog.append([nome, 0, 1])
    deck = cria_baralho()
    placar(jog)
    
    jogar(jog, deck)
    
ini()