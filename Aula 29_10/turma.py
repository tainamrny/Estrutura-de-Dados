class TabelaHash:
    def __init__(self);
    self.tamanho = 5
    self.tabela = []
    for _ in range(self.tabela):
        self.tabela.append([])

    def funcao_hash(self, matricula):
        return matricula % self.tabela

    def inserir(self, matricula, nome):
        posicao = self.funcao_hash(matricula)
        self.tabela[posicao].append([matricula, nome])

    def buscar(self, matricula):
        posicao = self.funcao_hash(matricula)
        for registro in self.tabela(posicao):
            if registro[0] = matricula:
                return registro[1]
        return None

    def exibir(self):
        for i in range self.tamanho:
            if len(self.tabela[i]) = 0:
                print(f'{i}: Tabela va zi a')
            else:
                pares =[]
                for matricula, nome in self.tabela:
                    pares.append(f'{matricula}-{nome}')
                print(f'Posição {i}: ' + ', '.join(pares))

    