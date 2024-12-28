# -------------------------------------------
# input para inserção de dados como no cSharp
variavelArmazenadora = input('text da pergunta/instrucao do input')
    # inputs sempre retornam para a variavel em STRING, pode precisar de conversão

# exemplo
nome = input('Insira seu nome: ')
idade = int(input('Insira sua idade: '))
peso = float(input('Insira seu peso: '))

# para saber o tipo é possivel PRINT o tipo
print(type(nome), type(idade), type(peso))

# tentativa não operacional, concat //py tem limitações
# print("nome: " + type(nome) + "idade: " + type(idade) + " peso: " + type(peso))



# -----------------
# condições IF ELSE
idadeUsuario = int(input('Insira sua idade: '))

if idadeUsuario >= 18: 
    print('Entrada permitida: ', idade, 'anos')

elif idadeUsuario > 15 and idadeUsuario < 18:
    print('Entrada com restrições: ', idade, 'anos')

else: 
    print('Entrada proibida: ', idade, 'anos')

# if pode ser feito no seguinte esquema boolean
casas = 10
familias = 6

tem_casas_suficientes = (casas >= familias)
print(tem_casas_suficientes)



# --------------
# arrays, listas
arrayNumeros = [7, 9, 16]
print(arrayNumeros[0])
print(arrayNumeros[2])
print(type(arrayNumeros))
print(arrayNumeros)

arrayDecimal = [12.4, 15.0]
arrayString = ['juan', 'bernardo']


# alterando valor de um item da lista
arrayNumeros[0] = 60
print('array atualizado', arrayNumeros)


# inserindo novos dados
arrayVazio = []

nome1 = input('Insira um nome: ')
arrayVazio.append(nome1)

nome2 = input('Insira outro nome: ')
arrayVazio.append(nome2)

print(arrayVazio)


# metodos para obtencao e extracao de dados basicos em arrays
print('total: ', len(arrayNumeros))
print('menor valor: ', min(arrayNumeros))



# ----------------------
# repetições FOR e WHILE

# FOR       loop percorre seqs, repetindo ações para cada elemento
# WHILE     loop executa ações Enquanto condição for verdadeira

# no FOR X é var temp para seq q progride com a repeticao até o limite do range
notas = []
for x in range (5):
    codigo_aluno = input('RM: ')
    nota = float(input('Nota: '))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print('Quantidade de alunos avaliados: ', len(notas))

# organização de lista dentro da lista
for n in notas: 
    codigo_aluno = n[0]
    nota = n[1]
    print('O RM: ', codigo_aluno, 'tirou a nota: ', nota)

# mesmo esquema com WHILE
notasWhile = []

contador = 1
while contador <= 5:
    codigo_alunoWhile = input('RM: ')
    notaWhile = float(input('Nota: '))
    resultadoWhile = [codigo_alunoWhile, notaWhile]
    notasWhile.append(resultadoWhile)
    contador += 1

print('Quantidade de alunos avaliados: ', len(notasWhile))



# --------------------------
# uso de bibliotecas basicas
import numpy as np
a = np.arange(10)

print(a)