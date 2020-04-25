def informações_aluno(*args):  # Função com lista de argumentos
    print(args)


informações_aluno(23, 'Fernando', True, 'T22')


def situação_aluno(**kwargs):  # Função com dicionário de argumentos
    print(kwargs)


situação_aluno(média=7.6, nome='Fernando', aprovado=True, turma=22)
