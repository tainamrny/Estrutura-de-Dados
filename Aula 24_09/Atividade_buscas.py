numeros = [40, 10, 70, 20, 60, 30, 50]

def busca_linear (lista, alvo):
    comparacoes = 0
    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == alvo:
            return i, comparacoes
    return -1, comparacoes #não achou/n é

def busca_binaria (lista, alvo):
    comparacoes = 0
    inicio = 0 #posição do primeiro elemento da lista
    fim = len(lista) - 1 #vê a posição do ultimo elemento
    while inicio <= fim:
        meio = (inicio + fim)//2 
        comparacoes += 1
        if lista[meio] == alvo:
            return meio, comparacoes
        elif lista[meio] < alvo:
            inicio = meio +1 #se o número é menor, joga pro da frente
        else:
            fim = meio - 1 #se for maior, volta para trás
        return -1, comparacoes

posicao_li, comparacoes_li = busca_linear(numeros, 60)

posicao_bi, comparacoes_bi = busca_binaria(numeros, 60)

print(f"Busca linear: posição {posicao_li}, comparações {comparacoes_li}")

print(f"Busca binária: posição {posicao_bi}, comparações {comparacoes_bi}") #não vai achar/conseguir, já que só funciona em listas ordenadas

#se o meio for[4] = 30 e ao comparar ele for menor que o alvo, se existir um 70 antes do 30 ele vai ser descartado junto 