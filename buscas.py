# -*- coding: utf-8 -*-


# Busca em Largura(sem nós repetidos)
def busca_largura(tab_inicial):
    fila = [tab_inicial]
    filaRepet = [tab_inicial]  # usada para verificar expanção de repetidos
    nos_exp = 0  # numero de nós expandidos

    while (len(fila) > 0):
        nodoTemp = fila.pop(0)  # retira do início da fila
        nos_exp = nos_exp + 1
        print('No expandido:', nos_exp)
        imprime_tabuleiro(nodoTemp)
        if verifica_objetivo(nodoTemp):
            print("*** Solução encontrada! Parabéns! ***")
            imprime_jogadas(nodoTemp)
            break
        else:
            #nodos_filhos = expandir(nodoTemp)
            for nt in nodos_filhos: #verifica se ja foi expandido
                ja_existe = False
                for x in filaRepet:
                    if tabuleiros_iguais(nt, x):
                        ja_existe = True
                        break  # se achou repetido para a busca
                if not ja_existe:
                    fila.append(nt)
                    filaRepet.append(nt)


#busca heurística a*
#def busca_astar(tab_inicial):