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
