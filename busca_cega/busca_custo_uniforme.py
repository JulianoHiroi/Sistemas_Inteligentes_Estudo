
import sys
import os

# Adiciona o diretório "pasta_pai" ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Sistemas_Inteligentes_Estudo.grafo import Grafo, grafo_padrao


#escolhe o menor e tira da fila
def escolhe_menor_custo(array):
    menor = array[0]
    for no in array:
        if(no.custo < menor.custo):
            menor = no
    array.remove(menor)
    return menor


def busca_custo_uniforme(grafo, no_inicial, no_final):
    inicio = grafo.buscar_vertice(no_inicial)
    inicio.custo = 0
    inicio.pai = None
    if(inicio == grafo.buscar_vertice(no_final)):
        print('O nó inicial é o nó final')
        return
    array = []
    array.append(inicio)
    while(array != []):
        no = escolhe_menor_custo(array)
        #print(" Explorei o nó: ", no.nome, " com custo: ", no.custo)
        if(no.nome == no_final):
            caminho = []
            while(no != None):
                caminho.append(no)
                no = no.pai
            caminho.reverse()
            return caminho
        no.estado = 1
        no.explorado = True
        for aresta in no.arestas:
            if(aresta.vertice2.estado == 0):
                #print(" Adicionei o nó: ", aresta.vertice2.nome, " com custo: ", no.custo + aresta.peso)
                if(aresta.vertice2.explorado == True and aresta.vertice2.custo > no.custo + aresta.peso):
                    aresta.vertice2.pai = no
                    aresta.vertice2.custo = no.custo + aresta.peso
                    continue
                aresta.vertice2.pai = no
                aresta.vertice2.custo = no.custo + aresta.peso
                aresta.vertice2.explorado = True
                array.append(aresta.vertice2)
            else:
                continue




def main():
    grafo = grafo_padrao()
    caminho = busca_custo_uniforme(grafo, 'A', 'F')
    print(caminho.__len__())
    print(caminho[caminho.__len__()-1].custo)

    for no in caminho:
        print(no.nome, '(' + str(no.custo) + ')' , end=' -  >')
    return 

    

if __name__ == "__main__":
    main()
