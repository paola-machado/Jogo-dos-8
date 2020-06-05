# -*- coding: utf-8 -*-
from estados import imprime_tabuleiro
from buscas import busca_largura #busca_astar


### Menu ###
tab_inicial = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]
tab_objetivo = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
print('Tabuleiro inicial: ')
imprime_tabuleiro(tab_inicial)
print('Tabuleiro objetivo: ')
imprime_tabuleiro(tab_objetivo)
print('----------------------------------------')
print('Informe qual algoritmo de busca deseja utilizar: ')
print("1: Busca Cega em Largura")
print("2: Busca Heurística (A*)")

op = int(input('Informe uma opção:'))
if op == 1:
    busca_largura(tab_inicial)
