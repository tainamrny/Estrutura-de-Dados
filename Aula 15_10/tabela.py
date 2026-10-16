#Ex02 Cria a classe
class TabelaHash: 
    def __init__(self):
            self.tamanho = 5 # Define o tamanho da tabela
            self.tabela =[]
            for _ in range(self.tamanho):
                  self.tabela.append([])

    #Ex03 Começa aqui
    def funcao_hash(self, RA): 
          return RA % self.tamanho

    #Ex04
    def inserir(self, RA, nome): 
          posicao = self.funcao_hash(RA) #Calcula a posição de cada RA na tabela usando a função hash 
          self.tabela[posicao].append([RA, nome]) #Atribui ambos ao final da posição

    #Ex05
    def buscar(self, RA):
        posicao = self.funcao_hash(RA)
        for registro in self.tabela[posicao]:
            if registro[0] == RA: #Faz comparação
                return registro[1]
        return None # Se não encontrar retorna none

    #Ex06
    def exibir(self):
        for i in range(self.tamanho):
            if len(self.tabela[i]) == 0:
                print(f"Posicao {i}: (vazia)")
        
            else:
                alunos = []
                for ra, nome in self.tabela[i]:
                    alunos.append(f"{ra}-{nome}")
                print(f"Posicao {i}: " + ", ".join(alunos))
        

    #Ex desafio, contar
    def contar(self):
        total = 0
        for lista in self.tabela: #para cada lista da tabela...
            total += len(lista) #Soma o tamanho de cada lista
        return total


t = TabelaHash()

print(t.tabela)
print(t.funcao_hash(412)) # Saída esperada: 2
print(t.funcao_hash(520)) # Saída esperada: 0

t.inserir(315, "Pedro")
t.inserir(520, "Rafael")
t.inserir(101, "Lucas")
t.inserir(207, "Marina")
t.inserir(412, "Julia")


#Marina e Julia não se sobrepoem porque inserimos a chave e o valor apenas no final do indice 2, os dados atribuidos pelo método inserir escrito acima, ao irem à um indice já ocupado se organizam como uma lista encadeada


#print(t.buscar(520))  # Saída esperada: Rafael
#print(t.buscar(105))  # Saída esperada: None 


#A quantidade de comparações depende de quantos pares foram atribuidos ao indice, nessa caso temos o 315 e o 520 no mesmo, totalizando duas comparações

print(t.contar())  

#t.inserir(625, "Sofia") #Adiciona novo par, porém pode ser feito pelo input no principal

print(t.contar())   
t.exibir()