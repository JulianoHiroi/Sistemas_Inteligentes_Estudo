# Faça uma classe de uma arvore que é inicializada com um nó raiz e possui um método que adiciona um nó filho a um nó
# Essa classe possuirá os seguintes métodos:
# - adicionar_filho com o parametro do No pai e do No filho
# - buscar_no com o parametro do nome do nó
# - remover_no com o parametro do nome do nó
# - listar_filhos com o parametro do nome do nó

class Arvore:
    def __init__(self, no_raiz):
        self.no_raiz = no_raiz
        self.tamanho = 1
    
    def adicionar_filho(self, pai, filho):
        pai.adicionar_filho(filho)
        self.tamanho += 1






#Faça uma classe de No de uma arvore que possui somente um atributo nome e um atributo filhos que é uma lista de nós
# Adicione um método que adiciona um nó filho a um nó

class No:
    def __init__(self, nome):
        self.nome = nome
        self.filhos = []
    
    def adicionar_filho(self, filho):
        self.filhos.append(filho)