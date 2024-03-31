# Implementação do algoritmo genético para a resolução do problema de busca local
# O problema escolhido é a resolução do problema das 8 rainhas
# O problema das oitos rainhas é um problema de busca em que o objetivo é posicionar 8 rainhas em um tabuleiro 8x8 de forma que nenhuma rainha ataque outra
# A representação do estado de um individuo será uma string de 8 caracteres, onde cada caracter representa a posição da rainha na coluna

import copy
import random

TAMANHO = 8
PROBABILIDADE_MUTACAO = 0.1

class No:
    def __init__(self, estado):
        self.estado = estado
        self.funcao_adaptativa = funcao_adaptação(self)



def combinacao(n, k):
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



# faça uma função que recebe uma string de TAMANHO caracteres e retorna uma matriz de TAMANHO x TAMANHO com 1 nas posições onde tem rainha e 0 onde não tem rainha
    
def string_para_tabuleiro(estado):
    tabuleiro = [[0 for i in range(TAMANHO)] for j in range(TAMANHO)]
    for i in range(TAMANHO):
        tabuleiro[int(estado[i] ) - 1][i] = 1
    return tabuleiro


# A função de adaptação será a quantidade de pares de rainhas não se atacam 
    
def funcao_adaptação(individuo):
    tabuleiro = string_para_tabuleiro(individuo.estado)
    #for i in range(TAMANHO):
        #print (tabuleiro[i])
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
    return 28 - heuristica
       


# A função de seleção aleatória irá escolher um individuo aleatório da população
def selecao_aleatoria(populacao):
    # soma das funções de adaptação de todos os individuos
    # a partir disso é calculado a probabilidade de cada individuo ser escolhido
    soma = 0 
    for i in range ( len(populacao)):
        soma = soma + populacao[i].funcao_adaptativa
    probabilidade = []
    for i in range ( len(populacao)):
        probabilidade.append(populacao[i].funcao_adaptativa / soma)
    acumulado = 0
    r = random.random()
    for i in range ( len(populacao)):
        acumulado = acumulado + probabilidade[i]
        if acumulado >= r:
            return populacao[i]
    


def cruzamento(x, y):
    # escolhe um ponto de corte aleatório
    corte = random.randint(2, 5)
    geneNovo = x.estado[0:corte] + y.estado[corte:TAMANHO]
    filho = No(geneNovo)
    return filho


def mutacao(filho):
    # escolhe um gene aleatório para mutar
    gene = random.randint(0, TAMANHO - 1)
    mudança = random.randint(1, TAMANHO)
    if filho.estado[gene] == str(mudança):
        mudança = (mudança + 1) % TAMANHO

    # sabendo que filho.estado é uma string, não é possivel mudar um caracter diretamente
    # então é necessário criar uma nova string com a mudança
    filho.estado = filho.estado[0:gene] + str(mudança) + filho.estado[gene + 1:TAMANHO]
    return filho


def algoritmo_genetico(populacao , limite):
    
    while limite > 0:
        limite = limite - 1
        nova_populacao = []
        for i in range ( len(populacao)):
            x = selecao_aleatoria(populacao)
            y = selecao_aleatoria(populacao)
            filho = cruzamento(x, y)
            if(PROBABILIDADE_MUTACAO > random.random()):
                filho = mutacao(filho)
            if (filho.funcao_adaptativa == 28):
                return filho
            nova_populacao.append(filho)
            populacao = nova_populacao
        
    return None
        
        

        


def main():
    populacao = []
    individuo1 = No("24748552")
    individuo2 = No("32752411")
    individuo3 = No("24415124")
    individuo4 = No("32543213")
    



    populacao.append(individuo1)
    populacao.append(individuo2)
    populacao.append(individuo3)
    populacao.append(individuo4)
    print("O tamanho da população é: ", len(populacao))
    
    while True: 
        solucao = algoritmo_genetico(populacao, 30000)
        if solucao == None:
            print("Não foi possivel achar uma solução")

        else:
            print("A solução é: ", solucao.estado)
            print("A função de adaptação é: ", solucao.funcao_adaptativa)
            break

    tabuleiro = string_para_tabuleiro(solucao.estado)
    for i in range(TAMANHO):
        print(tabuleiro[i])

    return 0

if __name__ == "__main__":
    main()  

