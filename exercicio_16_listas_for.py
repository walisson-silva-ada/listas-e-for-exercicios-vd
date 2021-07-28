nome = input("Nome do aluno: ")
idade = int(input("Idade do aluno: "))
while (no_provas <= 2):
    no_provas = int(input('Insira o número de provas (maior que 2): '))
notas = []
for i in range(no_provas):
    nota = float(input("Digite uma nota de prova: "))
    notas.append(nota)
notas_removidas = notas[:]
notas_removidas.remove(max(notas_removidas))
notas_removidas.remove(min(notas_removidas))
media = sum(notas_removidas)/len(notas_removidas)
dentro_media = (media >= 5)
lista = [nome, idade, notas, media, dentro_media]
print(lista)
