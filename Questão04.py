import time


def mostrar_solução(tabuleiro, n):
    for i in range(n):
        for j in range(n):
            print(f'{tabuleiro[i][j]} ', end='')
        print()


def seguro(tabuleiro, linha, coluna, n):
    # Verificar se há alguma rainha na linha
    for j in range(coluna):
        if tabuleiro[linha][j] == 1:
            return False

    # Verificar se há alguma rainha na diagonal principal acima
    i = linha
    j = coluna
    while i >= 0 and j >= 0:
        if tabuleiro[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Verificar se há alguma rainha na diagonal secundária abaixo
    i = linha
    j = coluna
    while i < n and j >= 0:
        if tabuleiro[i][j] == 1:
            return False
        i += 1
        j -= 1

    # Se nenhuma das condições for satisfeita
    return True


def buscar_solução(tabuleiro, coluna, n):
    if coluna >= n:
        return True

    for i in range(n):
        if seguro(tabuleiro, i, coluna, n):
            tabuleiro[i][coluna] = 1
            if buscar_solução(tabuleiro, coluna + 1, n):
                return True
            tabuleiro[i][coluna] = 0
    return False


def resolver():
    n = int(input('Tamanho do tabuleiro: '))
    tabuleiro = [n * [0] for _ in range(n)]

    if not buscar_solução(tabuleiro, 0, n):
        print('Não há solução. ')
        return False

    mostrar_solução(tabuleiro, n)
    return True


#resolver()
print()


def resolver_em_ate_1min():
    n = 0
    while True:
        n += 1
        tabuleiro = [n * [0] for _ in range(n)]
        ini = time.time()
        buscar_solução(tabuleiro, 0, n)
        fim = time.time()
        tempo = fim - ini

        if tempo >= 60:
            print(f'--> {n}: {tempo}')
        else:
            print(f'{n}: {tempo}')


resolver_em_ate_1min()
'''
Analisando o resultado obtido pela aplicação dessa função (resolver_em_ate_1min()), percebemos que, 
apesar de o tabuleiro 22x22 demorar mais de 1min, os seguintes (23, 24, 24, 25, 26 e 27) demoram menos 
de 1min. Entretanto, a partir do tabuleiro 28x28, a solução demora muito mais de 1min para ser 
determinada. Assim, o maior caso que é possível resolver em menos de 1min é o tabuleiro 27x27.

Um resultado econtrado está registrado abaixo (tempo em segundos):
 1: 0.0
 2: 0.0
 3: 0.0
 4: 0.0
 5: 0.0
 6: 0.0
 7: 0.0
 8: 0.0
 9: 0.0
10: 0.0
11: 0.0
12: 0.0
13: 0.01562356948852539
14: 0.031241655349731445
15: 0.03124260902404785
16: 0.23432207107543945
17: 0.1405932903289795
18: 1.2965669631958008
19: 0.07810640335083008
20: 7.168242454528809
21: 0.3280484676361084
--> 22: 72.48304629325867
23: 1.1872224807739258
24: 19.807865381240845
25: 2.5463223457336426
26: 22.572803735733032
27: 27.868481636047363
--> 28: 194.3743703365326
--> 29: 104.9285819530487
'''
