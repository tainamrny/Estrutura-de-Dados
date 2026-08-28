class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f'Node list({self.data!r})'

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        novo = Node(data)
        if self.head is None:
            self.head = novo
            return
        atual = self.head
        while atual.next is not None
            atual = atual.next
        atual.next = novo

    def __iter__(self):
        

lista.append('impressora')
lista.append('senha')
lista.append('login')

for item in lista:
    print(item)
