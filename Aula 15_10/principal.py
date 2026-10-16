from tabela import TabelaHash
t = TabelaHash()

while True:
    RA_texto = input("Digite o RA ou 'fim' para encerrar: ")
    if RA_texto == "fim":
        break
    nome = input("Nome: ")
    t.inserir(int(RA_texto), nome)

#print()
#t.exibir()
print(t.contar())   
t.exibir()


RA = int(input("RA para buscar: "))
nome = t.buscar(RA)
if nome is not None:
    print(f"Aluno encontrado: {nome}")
else:
    print("RA nao cadastrado.")