from turma import TabelaHash
t = TabelaHash()

while True:
    matricula_t = input('Digite a matricula ou fim:')
    if matricula_t == 'fim':
        break
    nome = input('nome: ')
    t.inserir(int(matricula_t, nome))

t.exibir()

matricula = int(input('matricula para buscar:'))
nome = t.buscar(matricula)
if nome is not None:
    print(f'Aluno: {nome}')
else: 
    print('Aluno não cadastrado')