class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        novo = Node(data)
        if self.head is None:
            self.head = novo
            return
        atual = self.head
        while atual.next is not None:
            atual = atual.next
        atual.next = novo

    def imprimir(self):
        if self.head is None:
            print("Lista vazia")
            return
        atual = self.head
        while atual is not None:
            print(atual.data)
            atual = atual.next


lista = LinkedList()
lista.append('Primeiro')
lista.append('Segundo')
lista.append('Terceiro')

lista.imprimir()

#Inserção e remoção são mais simples, inserir um item sempre vai para o fim da lista é remoção depende se o item a ser removido é o primeiro
#Funciona para uma lista de atendimento