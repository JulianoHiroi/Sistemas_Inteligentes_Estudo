
import copy
# Crie uma classe de grafo que implemente as seguintes operações:
# - Adicionar vértices
# - Adicionar arestas que serão adicionadas a um vértice

TAMANHO = 3
CUSTO_ACAO = 1
SOLUCAO = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
class No:
    def __init__(self, estado):
        self.estado = estado
        self.heuristica = heuristica(estado)
        self.pai = None
        self.filhos = []
        self.custo = 0
        self.distancia = 0

    def __str__(self):
        return f'{self.estado}'



#implementação do algoritmo A* para o problema do quebra-cabeça de 8 peças
# O problema do quebra-cabeça de 8 peças é um problema de busca em que o objetivo é mover as peças de um tabuleiro 3x3 para que fiquem em ordem crescente
# O tabuleiro é representado por uma matriz 3x3


#Algorirmo A*:
# inicializa o grafo com o tabuleiro inicial
# inicializa o nó inicial com o tabuleiro inicial

def inicia_no( no , noPai , custo):
    no.pai = noPai
    no.heuristica = heuristica(no.estado)
    no.distancia = noPai.distancia + custo
    no.custo = no.heuristica + no.distancia
    noPai.filhos.append(no)



def adicionar_nos_filhos(no):
    x = 0
    y = 0
    for i in range(TAMANHO):
        for j in range(TAMANHO):
            if no.estado[i][j] == 0:
                x = i
                y = j
    if x > 0:
        aux = copy.deepcopy(no.estado)
        aux1 = aux[x][y]
        aux[x][y] = aux[x-1][y]
        aux[x-1][y] = aux1 
        noAux = No(aux)
        inicia_no(noAux, no, CUSTO_ACAO)
    if x < 2:
        aux = copy.deepcopy(no.estado)
        aux1 = aux[x][y]
        aux[x][y] = aux[x+1][y]
        aux[x+1][y] = aux1 
        noAux = No(aux)
        inicia_no(noAux, no, CUSTO_ACAO)
    if y > 0:
        aux = copy.deepcopy(no.estado)
        aux1 = aux[x][y]
        aux[x][y] = aux[x][y-1]
        aux[x][y-1] = aux1 
        noAux = No(aux)
        inicia_no(noAux, no, CUSTO_ACAO)
    if y < 2:
        aux = copy.deepcopy(no.estado)
        aux1 = aux[x][y]
        aux[x][y] = aux[x][y+1]
        aux[x][y+1] = aux1 
        noAux = No(aux)
        inicia_no(noAux, no, CUSTO_ACAO)



def heuristica(tabelueiro):
    h = 0
    for i in range(3):
        for j in range(3):
            if tabelueiro[i][j] != 0:
                h += abs(j - tabelueiro[i][j]%3 ) + abs(i - (tabelueiro[i][j] // 3))
    return h



def busca_A_estrela(tabelueiro):
    no = No(tabelueiro)
    no.custo = no.heuristica
    no.distancia = 0
    no.pai = None
    array = []
    array.append(no)
    while len(array) > 0:
        no = escolhe_menor_custo(array)
        if no.estado == SOLUCAO:
            print ("Solução encontrada")
            return no
        adicionar_nos_filhos(no)
        for filho in no.filhos:
            array.append(filho)
    return None
     

def escolhe_menor_custo(array):
    menor = array[0]
    for no in array:
        if(no.custo < menor.custo):
            menor = no
    array.remove(menor)
    return menor


def main():
    tabuleiro = [[4, 5 , 6], [7, 1, 2], [3, 0, 8]]
    no = busca_A_estrela(tabuleiro)
    
    print("O custo da solução é: ", no.distancia)

if __name__ == "__main__":
    main()



