# O problema das oitos rainhas é um problema de busca em que o objetivo é posicionar 8 rainhas em um tabuleiro 8x8 de forma que nenhuma rainha ataque outra
# O tabuleiro é representado por uma matriz 8x8
# Cada rainha ficará em uma coluna e irá mexer sempre na sua coluna para achar a melhor posição
# Uma matriz auxiliar de heuristica é criada para cada nó, onde cada posição da matriz representa a quantidade de ataques de pares de rainhas acontecem se a rainha da coluna mudar para essa posioção

import copy

TAMANHO = 8


class No:
    def __init__(self, estado):
        self.estado = estado
        self.heuristica = 0
def combinacao(n, k):
    """
    Calcula o coeficiente binomial (combinação) C(n, k).
    
    Args:
        n (int): Número total de elementos no conjunto.
        k (int): Número de elementos a serem escolhidos.
        
    Returns:
        int: O valor da combinação C(n, k).
    """
    if k < 0 or k > n:
        return 0
    else:
        # Calcula fatorial de n
        fatorial_n = 1
        for i in range(1, n + 1):
            fatorial_n *= i
        
        # Calcula fatorial de k
        fatorial_k = 1
        for i in range(1, k + 1):
            fatorial_k *= i
        
        # Calcula fatorial de n - k
        fatorial_nk = 1
        for i in range(1, n - k + 1):
            fatorial_nk *= i
        
        # Calcula C(n, k)
        combinacao = fatorial_n // (fatorial_k * fatorial_nk)
        return combinacao

def heuristica(tabuleiro):
# calcula a quantidade de pares de rainhas que se atacam e coloca na matriz de heuristica
    heuristica = 0
    for i in range(TAMANHO):
        count_rainhas = 0
        for j in range(TAMANHO):
            if tabuleiro[i][j] == 1:
                count_rainhas += 1
        # se tiver mais de uma rainha na linha , é calculado a quantidade de combinações é possivel fazer com as rainhas
        #print("Quantidade de rainhas na linha: ", count_rainhas)
        if count_rainhas > 1:
            heuristica += combinacao(count_rainhas, 2)
# calcula a quantidade de pares de rainhas que se atacam na diagonal principal
# começando da linha 7 e coluna 0 até a linha 0 e coluna 7
    for i in range(-TAMANHO + 1, TAMANHO):
        count_rainhas = 0
        if i < 0:
            for j in range(TAMANHO + i):
                if tabuleiro[j][j - i] == 1:
                    count_rainhas += 1
        else:
            for j in range(TAMANHO - i):
                if tabuleiro[j + i][j] == 1:
                    count_rainhas += 1
        #print("Quantidade de rainhas na diagonal principal: ", count_rainhas)
        if count_rainhas > 1:
            heuristica += combinacao(count_rainhas, 2)

# calcula a quantidade de pares de rainhas que se atacam na diagonal secundaria
# começando da linha 0 e coluna 0 até a linha 7 e coluna 7
    for i in range(1, 2 * TAMANHO - 1):
        count_rainhas = 0
        if i < TAMANHO:
            for j in range(i + 1):
                if tabuleiro[j][i - j] == 1:
                    count_rainhas += 1
        else:
            for j in range(2 * TAMANHO - i - 1):
                if tabuleiro[i - TAMANHO + j][TAMANHO - 1 - j] == 1:
                    count_rainhas += 1
        #print("Quantidade de rainhas na diagonal secundaria: ", count_rainhas)
        if count_rainhas > 1:
            heuristica += combinacao(count_rainhas, 2)
    return heuristica


def achar_melhores(no):
    #acha os melhores vizinhos
    # se a heuristica do vizinho for menor que a heuristica do no atual, o vizinho é adicionado a lista de melhores
    # ira percorrer a matriz e calcular a heuristica de cada estado de tabuleiro que é possivel fazer com um movimetno de rainha na mesma coluna
    melhor = None
    menor = no.heuristica
    for i in range(TAMANHO):
        for j in range(TAMANHO):
            if no.estado[i][j] == 0:
                aux = copy.deepcopy(no.estado)
                #print(aux)
                for k in range(TAMANHO):
                    if aux[k][j] == 1:
                        local_rainha = k
                        break
                aux[i][j] = 1
                aux[local_rainha][j] = 0
                heuristica_aux = heuristica(aux)
                if heuristica_aux <= menor:
                    '''if heuristica_aux < menor:
                        #print("A heuristica é: ", heuristica_aux)
                        melhores = []'''
                    melhor = No(aux)
                    melhor.heuristica = heuristica_aux
                    menor = heuristica(aux)

    return melhor

def buca_subida_encosta(estado):
    no = No(estado)
    no.heuristica = heuristica(estado)
    while True:
        melhor = achar_melhores(no)
        if melhor == None:
            print("O estado é: ", no.estado)
            print ("A heuristica é: ", no.heuristica)
            print ("Não foi possivel achar um melhor estado")
            break
        no = melhor
                
    




def main():
    tabuleiro = [[0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 1, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
    buca_subida_encosta(tabuleiro)

    return 0    


if __name__ == "__main__":
    main()