

def grafo_padrao():
    grafo = Grafo()
    grafo.adicionar_vertice('A')
    grafo.adicionar_vertice('B')
    grafo.adicionar_vertice('C')
    grafo.adicionar_vertice('D')
    grafo.adicionar_vertice('E')
    grafo.adicionar_vertice('F')
    grafo.adicionar_vertice('G')
    grafo.adicionar_vertice('H')
    grafo.adicionar_aresta('A', 'C', 1)
    grafo.adicionar_aresta('C', 'B', 4)
    grafo.adicionar_aresta('C', 'G', 1)
    #grafo.adicionar_aresta('B', 'G', 1)
    grafo.adicionar_aresta('G', 'B', 1)
    grafo.adicionar_aresta('B', 'D', 2)
    grafo.adicionar_aresta('B', 'E', 6)
    grafo.adicionar_aresta('G', 'H', 5)
    grafo.adicionar_aresta('E', 'F', 3)
    return grafo




# Crie uma classe de grafo que implemente as seguintes operações:
# - Adicionar vértices
# - Adicionar arestas que serão adicionadas a um vértice

class Grafo:
    def __init__(self):
        self.vertices = []
    
    def adicionar_vertice(self, nome):
        vertice = Vertice(nome)
        self.vertices.append(vertice)


    def adicionar_aresta(self, nome_vertice1, nome_vertice2, peso):
        vertice1 = self.buscar_vertice(nome_vertice1)
        vertice2 = self.buscar_vertice(nome_vertice2)
        aresta = Aresta(vertice1, vertice2, peso)
        vertice1.arestas.append(aresta)
        vertice2.arestas.append(aresta)
    
    def buscar_vertice(self, nome):
        for vertice in self.vertices:
            if vertice.nome == nome:
                return vertice
        return None
    


class Vertice:
    def __init__(self, nome):
        self.nome = nome
        self.arestas = []
        self.estado =  0 
        self.pai = None
        self.custo = 0
        self.explorado = False
    
    def __str__(self):
        return self.nome

class Aresta:
    def __init__(self, vertice1, vertice2, peso):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.peso = peso
    
    def __str__(self):
        return f'{self.vertice1} - {self.vertice2}'