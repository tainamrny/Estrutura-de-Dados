#Lista pequena e desordenada
produtos = [12, 7, 25, 3, 18, 40]
def busca_linear(lista, alvo):
    comparacoes = 0
    for i in range(len(lista)):
        comparacoes += 1 # contamos CADA verificação
        if lista[i] == alvo:
            return i, comparacoes
            
    return -1, comparacoes # percorreu tudo e não achou

for alvo in [18, 12, 40, 99]:
    posicao, comp = busca_linear(produtos, 7)
    print(f"Alvo {alvo}: posição {posicao}, comparações {comp}")