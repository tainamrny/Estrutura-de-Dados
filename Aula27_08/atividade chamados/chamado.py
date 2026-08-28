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
        posicao = 1
        while atual is not None:
            yield posicao, atual.chamado #pega o que já está lá e n perde nos loops
            #print(atual.chamado, end =' ->')
            atual = atual.next
            posicao += 1
             #a posição veio aqui para ser chamada junto do chamado, assim permite colocar as duas informações no for como uma tupla
            
            # joguei o print '->' no principal já que é lá que está meu for
    
   
            


    