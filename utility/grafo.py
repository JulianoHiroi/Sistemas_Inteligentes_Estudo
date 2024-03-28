
#Faça um função que instancia um grafo padrão completo com 8 vertices e retorna o grafo

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
    grafo.adicionar_aresta('A', 'B', 1)
    grafo.adicionar_aresta('A', 'C', 1)
    grafo.adicionar_aresta('A', 'D', 1)
    grafo.adicionar_aresta('A', 'E', 1)
    grafo.adicionar_aresta('A', 'F', 1)
    grafo.adicionar_aresta('A', 'G', 1)
    grafo.adicionar_aresta('A', 'H', 1)
    grafo.adicionar_aresta('B', 'C', 1)
    grafo.adicionar_aresta('B', 'D', 1)
    grafo.adicionar_aresta('B', 'E', 1)
    grafo.adicionar_aresta('B', 'F', 1)
    grafo.adicionar_aresta('B', 'G', 1)
    grafo.adicionar_aresta('B', 'H', 1)
    grafo.adicionar_aresta('C', 'D', 1)
    grafo.adicionar_aresta('C', 'E', 1)
    grafo.adicionar_aresta('C', 'F', 1)
    grafo.adicionar_aresta('C', 'G', 1)
    grafo.adicionar_aresta('C', 'H', 1)
    grafo.adicionar_aresta('D', 'E', 1)
    grafo.adicionar_aresta('D', 'F', 1)
    grafo.adicionar_aresta('D', 'G', 1)
    grafo.adicionar_aresta('D', 'H', 1)
    grafo.adicionar_aresta('E', 'F', 1)
    grafo.adicionar_aresta('E', 'G', 1)
    grafo.adicionar_aresta('E', 'H', 1)
    grafo.adicionar_aresta('F', 'G', 1)
    grafo.adicionar_aresta('F', 'H', 1)
    grafo.adicionar_aresta('G', 'H', 1)
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
    
    def __str__(self):
        return self.nome

class Aresta:
    def __init__(self, vertice1, vertice2, peso):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.peso = peso
    
    def __str__(self):
        return f'{self.vertice1} - {self.vertice2}'