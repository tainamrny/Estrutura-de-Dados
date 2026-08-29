class Node:
    def __init__(self, chamado):
        self.chamado = chamado
        self.next = None

class listaChamados:
    def __init__(self):
        self.chamado = None #inicio

    def inserir_fim(self, chamado):
        novo = Node(chamado)
        if self.chamado is None:
            self.chamado = novo #chama o novo nome
            return
        
        atual = self.chamado

        while atual.next is not None:
            atual = atual.next

        atual.next = novo


    def __iter__(self):  #ele que chama a variável criada tipo, chama o chamado sem alterar o valor "uma nova caixinha"
        atual =self.chamado
    
        while atual is not None:
            yield atual.chamado
            atual = atual.next #funfact que fiquei 30min aqui rodando infinito só pela identação

    def buscar(self, chamado):
        atual = self.chamado
        posicao = 0
        while atual is not None:
            if atual.chamado == chamado:
                return posicao
            atual = atual.next
            posicao += 1
        return -1  
            


    