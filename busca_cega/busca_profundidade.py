import sys
import os

# Adiciona o diretório "pasta_pai" ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Sistemas_Inteligentes_Estudo.grafo import Grafo, grafo_padrao

def funcao_recursiva ( grafo , limite, no_objetivo , no):
    if no == no_objetivo:
        return no_objetivo
    if limite == 0:
        return None
    else:
       for aresta in no.arestas:
            if(aresta.vertice2.estado == 0):
                aresta.vertice2.estado = 1
                aresta.vertice2.pai = no
                solucao = funcao_recursiva(grafo, limite - 1, no_objetivo, aresta.vertice2)
                if solucao != None:
                    return solucao
    return None


# a função busca_profundidade recebe um grafo, um nó inicial e um nó final e retorna o caminho entre o nó inicial e o nó final
# e será feito a partir de uma função recursiva que terá um limite de profundidade para evitar loops infinitos
def busca_profundidade(grafo, no_inicial, no_final):
    solucao =  funcao_recursiva(grafo, 6, grafo.buscar_vertice(no_final), grafo.buscar_vertice(no_inicial))
    if solucao == None:
        print("Nao foi possivel encontrar o nó final")
        return
    caminho = []
    while(solucao != None):
        caminho.append(solucao)
        solucao = solucao.pai   
    return caminho

def main():
    grafo = grafo_padrao()
    caminho = busca_profundidade(grafo, 'A', 'F')
    print(caminho.__len__())
    for no in caminho:
        print(no.nome, '(' + str(no.custo) + ')' , end=' -  >')
    return 

    

if __name__ == "__main__":
    main()
