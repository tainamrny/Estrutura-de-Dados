class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        novo = Node(data)
        novo.next = self.head
        novo.head = novo
    
    def inserir_fim (self, data):
        novo = Node(data)
        if self.head is None:
            self.head = novo
            return
        atual = self.head
        while atual.next is not None:
            atual = atual.next
        atual.next = novo