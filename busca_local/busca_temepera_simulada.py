# O problema das oitos rainhas é um problema de busca em que o objetivo é posicionar 8 rainhas em um tabuleiro 8x8 de forma que nenhuma rainha ataque outra
# O tabuleiro é representado por uma matriz 8x8
# Cada rainha ficará em uma coluna e irá mexer sempre na sua coluna para achar a melhor posição
# Uma matriz auxiliar de heuristica é criada para cada nó, onde cada posição da matriz representa a quantidade de ataques de pares de rainhas acontecem se a rainha da coluna mudar para essa posioção
# A tempura simulada é um algoritmo de busca local que tenta achar o melhor estado de um problema de otimização
import copy
import math
import random


TAMANHO = 8
TEMP_INICIAL = 1000
ALPHA = 0.99



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



def escalonamento(tempo):
    return TEMP_INICIAL * (ALPHA ** tempo)
def sucessor_aleatorio(no):
    #achar um sucessor aleatorio
    auxNo = copy.deepcopy(no)

    y = random.randint(0, 7)
    x = random.randint(0, 7)
    for i in range(TAMANHO):
        if auxNo.estado[i][y] == 1:
            auxNo.estado[i][y] = 0
            
            while x == i:
                x = random.randint(0, 7)
            auxNo.estado[x][y] = 1
            break
            
    auxNo.heuristica = heuristica(auxNo.estado)

    return auxNo
    

def calcular_probabilidade(delta_E, temperatura):
    # Calcular o valor de e elevado a delta_E dividido pela temperatura
    return math.exp(delta_E / temperatura)

def busca_tempera_simulada(problema):
    atual = No(problema)
    atual.heuristica = heuristica(atual.estado)
    for i in range(5000):
        temp = escalonamento(i) 
        if temp == 0 or atual.heuristica == 0:
            print("Tempo: ", i)
            #print (atual.estado)
            break
        proximo = sucessor_aleatorio(atual)
        DeltaE =  atual.heuristica - proximo.heuristica 
        if DeltaE > 0: 
            atual = proximo
        else:
            # Calcular a probabilidade de aceitar o estado 
            # Se a probabilidade for maior que um número aleatório, aceitar o estado
            probabilidade = calcular_probabilidade(DeltaE, temp)
            numero_aleatorio = random.random()
            if probabilidade > numero_aleatorio:
                atual = proximo
    return atual


    
                
    




def main():
    tabuleiro = [[0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 0, 0],
                 [0, 1, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
    
    resultado = busca_tempera_simulada(tabuleiro)
    for i in range(TAMANHO):
        print(resultado.estado[i])
    
    print(combinacao(8, 2))

    return 0    


if __name__ == "__main__":
    main()