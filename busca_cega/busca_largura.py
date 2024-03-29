# importe as classes Grafo do arquivo grafo.py que está na pasta utility no diretorio pai do arquivo atual colocando o packge no sys.path


import sys
import os

# Adiciona o diretório "pasta_pai" ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Sistemas_Inteligentes_Estudo.grafo import Grafo, grafo_padrao








# a função busca_em_arvore recebe um grafo, um nó inicial e um nó final e retorna o caminho entre o nó inicial e o nó final
# a busca é feita a partir de uma pilha que 


def busca_em_arvore(grafo, no_inicial, no_final):
    inicio = grafo.buscar_vertice(no_inicial)
    inicio.custo = 0
    inicio.pai = None
    if(inicio == grafo.buscar_vertice(no_final)):
        print('O nó inicial é o nó final')
        return
    pilha = []
    pilha.append(inicio)
    while(pilha != []):
        no = pilha.pop()
        if(no.nome == no_final):
            caminho = []
            while(no != None):
                caminho.append(no)
                no = no.pai
            caminho.reverse()
            return caminho
        no.estado = 1
        for aresta in no.arestas:
            if(aresta.vertice2.estado == 0):
                aresta.vertice2.pai = no
                aresta.vertice2.custo = no.custo + aresta.peso
                pilha.append(aresta.vertice2)
            else:
                continue
        




def main():
    grafo = grafo_padrao()
    caminho = busca_em_arvore(grafo, 'A', 'D')
    print(caminho.__len__())
    custo = caminho[caminho.__len__()-1].custo
    print(custo)
    return 

    

if __name__ == "__main__":
    main()
