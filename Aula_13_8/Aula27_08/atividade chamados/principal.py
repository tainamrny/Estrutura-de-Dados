from chamado import listaChamados
lista = listaChamados()

while True:
    chamado_busca = input('Insira o nome do chamado:')
    if chamado_busca == 'fim':
        break
    
    lista.append(chamado_busca)
    
for nome in lista:
    print(nome)
    
    
