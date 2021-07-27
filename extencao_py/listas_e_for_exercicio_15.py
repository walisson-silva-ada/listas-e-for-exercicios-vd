#exercicio 15
nome = input("digite o nome da aluna: ")
idade = float(input("digite a idade da aluna: "))
qtde = float(input("quantas provas a aluna fez: "))
aux = 0
notas = []
while aux < qtde:
    notas.append(float(input("digite a nota da aluna: ")))
    aux += 1

media = sum(notas)/qtde
if media > 5:
    x = True
l = [nome, idade, notas, media, x]

print(l)
