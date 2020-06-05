# -*- coding: utf-8 -*-


# Imprime o tabuleiro
def imprime_tabuleiro(tab):
    print(tab[0])
    print(tab[1])
    print(tab[2])


def imprime_jogadas(tab):
    print("\nAs jogadas foram:")
    pilha = []
    while tab[3][1] != None:
        pilha.append(tab)
        tab = tab[3][1]
    pilha.append(tab)
    while len(pilha) > 0:
        temp = pilha.pop()
        imprime_tabuleiro(temp)


# Verifica se os dois tabuleiros são iguais
def tabuleiros_iguais(tab1, tab2):
    sao_iguais = True
    for i in range(3):
        for j in range(3):
            if tab1[i][j] != tab2[i][j]:
                sao_iguais = False
    return sao_iguais


def verifica_objetivo(tab):
    a = True
    if tab[0][0] != 1: a = False
    if tab[0][1] != 2: a = False
    if tab[0][2] != 3: a = False
    if tab[1][0] != 8: a = False
    if tab[1][1] != 0: a = False
    if tab[1][2] != 4: a = False
    if tab[2][0] != 7: a = False
    if tab[2][1] != 6: a = False
    if tab[2][2] != 5: a = False
    return a
