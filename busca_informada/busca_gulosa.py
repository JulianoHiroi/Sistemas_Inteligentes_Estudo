import sys
import os

# Adiciona o diretório "pasta_pai" ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Sistemas_Inteligentes_Estudo.grafo import Grafo, grafo_distancia


#escolha heuristica usada nessa função foi de escolher o no com a menor distancia em linha reta
def escolha_heuristica(arestas):
    menor = arestas[0]
    for aresta in arestas:
        if(menor.vertice2.distancia > aresta.vertice2.distancia and aresta.vertice2.estado == 0):
            menor = aresta

    return menor

def busca_gulosa(grafo, no_inicial, no_final, limite):
    no = grafo.buscar_vertice(no_inicial)
    no.custo = 0
    no.pai = None
    if(no == grafo.buscar_vertice(no_final)):
        print('O nó inicial é o nó final')
        return
    while no.nome != no_final and limite > 0:
        no.estado = 1
        limite -= 1
        aresta = escolha_heuristica(no.arestas)
        if(aresta.vertice2.estado == 1):
            continue
        aresta.vertice2.pai = no    
        no = aresta.vertice2
       
    caminho = []

    while(no != None):
        print(no.nome)
        caminho.append(no)
        no = no.pai
    caminho.reverse()
    return no

def main():
    grafo = grafo_distancia()
    caminho = busca_gulosa(grafo, 'A', 'F', 10)

    return 

    

if __name__ == "__main__":
    main()
