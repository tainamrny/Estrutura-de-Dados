def funcao_hash(chave, tamanho):
    return sum(ord(char) for char in chave)% tamanho

class TabelaHash:
    def __init__(self, tamanho):
        self.size = tamanho
        self.table =[[]for _ in range(tamanho)]

    def setar_item(self, chave, valor):
        indice = funcao_hash(chave, self.size)

        for par in self.table[indice]:
            if par[0] == chave:
                par[1] = valor
                return

        self.table[indice].append([chave, valor])

    def obter_item(self, chave):
        indice= funcao_hash(chave, self.size)

        for par in self.table[indice]:
            if par[0] == chave:
                return par[1]
        return None

    def remover_item(self, chave):
            indice= funcao_hash(chave, self.size)
    
            for par in self.table[indice]:
                if par[0] == chave:
                    self.table[indice].remove(par)
                    return

    def __repr__(self): #representação da tabela hash para exibição
        return str(self.table)

tabela_hash = TabelaHash(5) #tamanho
tabela_hash.setar_item("ju", "33")
tabela_hash.setar_item("renan", "58")

print(tabela_hash)

print("idade: ", tabela_hash.obter_item("ju"))

tabela_hash.remover_item("renan")

print(tabela_hash)