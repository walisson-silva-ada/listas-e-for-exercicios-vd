nome = input('Entre com o nome do aluno: ')
lista_nome = [nome]
idade = int(input('Entre com a idade do aluno: '))
lista_idade = [idade]
qtd_provas = int(input('Entre com a qtd de provas que o aluno realizou: '))

provas = []
for i in range(qtd_provas):
    nota = float(input('Entre com uma nota: '))
    provas.append(nota)

mean_notas = sum(provas)/len(provas)

dentro_media = mean_notas > 5

print(dentro_media)

lista_geral = [nome, idade, provas, mean_notas, dentro_media]

print(lista_geral)
