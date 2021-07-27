#exercicio 17
cpf = input("digite seu cpf sem hifem ou pontos: ")
while len(cpf) != 11:
    print("cpf invalido")
    cpf = input("digite seu cpf: ")

l = list(cpf)
aux1 = 0
aux2 = 10
s1 = 0
while aux1 < 9:
    s1 = s1 + (int(l[aux1])*aux2)
    #print(aux2, " * ", l[aux1])
    aux1 += 1
    aux2 -= 1

s2 = (s1*10)%11

aux1 = 0
aux2 = 11
s3 = 0
if s2 == 10:
    s2 = 0
if s2 == int(l[9]):
    while aux1 < 10:
        s3 = s3 + (int(l[aux1])*aux2)
        #print(aux2, " * ", l[aux1])
        #print(s3)
        aux1 += 1
        aux2 -= 1
else:
    print("cpf invalido")
x = (s3*10)%11
if x == 10:
    x = 0
if x == int(l[10]):
    print("cpf valido")
else:
    print("cpf invalido")