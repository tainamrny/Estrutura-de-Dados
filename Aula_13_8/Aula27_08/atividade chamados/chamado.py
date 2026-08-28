class Node:
    def __init__(self, chamado):
        self.chamado = chamado
        self.next = None

class listaChamados:
    def __init__(self):
        self.chamado = None

    def append(self, chamado):
        novo = Node(chamado)
        if self.chamado is None:
            self.chamado = novo #chama o novo nome
            return
        
        atual = self.head

        while atual.next is not None:
            atual = atual.next

        atual.next = novo

def inserir_fim(self):
    atual.next = novo

def __iter__(self):
    atual =self.chamado
    while atual is not None:
        print(atual.chamado, end =' ->')
    atual = atual.next
    print('none')
    
def buscar(self, chamado):
    atual = self.head
    posicao= 0
    while atual is not None:
        if atual == chamado:
            return posicao
        atual = atual.next
        posicao += 1
    return -1
        


    