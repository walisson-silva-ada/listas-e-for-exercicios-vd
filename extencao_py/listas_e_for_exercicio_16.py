#exercicio 16
nome = input("digite o nome da aluna: ")
idade = float(input("digite a idade da aluna: "))
qtde = 0
while qtde<3:
    qtde = float(input("quantas provas a aluna fez: "))
aux = 0
notas = []
while aux < qtde:
    notas.append(float(input("digite a nota da aluna: ")))
    aux += 1
n = []

for y in notas:
    n.append(y)

n.remove(max(n))
n.remove(min(n))

media = sum(n)/(qtde - 2)
if media > 5:
    x = True
else:
    x = False
l = [nome, idade, notas, media, x]

print(l)