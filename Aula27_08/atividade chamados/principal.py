from chamado import listaChamados
lista = listaChamados()


while True:
    chamado = input('Insira o nome do chamado:')
    if chamado == 'fim':
        break

    
    lista.inserir_fim(chamado)


for chamado in lista:
    print(chamado, end=' -> ')
print('none')#depois de ler todos chamados que teve no input, printa o none


chamado_busca = input('Digite a busca:')

posicao = lista.buscar(chamado_busca)# pucha o buscar do chamado.py
if posicao == -1:
    print('Chamado não encontrado')
else:
    print(f' O chamado {chamado_busca} foi encontrado na posição {posicao}')
        
    
    
