from chamado import listaChamados
lista = listaChamados()


while True:
    chamado = input('Insira o nome do chamado:')
    if chamado == 'fim':
        break
    
    lista.inserir_fim (chamado)

for posicao,chamado in (lista):
    print(posicao, chamado, end =' -> ')
print('none') #depois de ler todos chamados que teve no input, printa o none
    
