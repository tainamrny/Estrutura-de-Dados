ordenada = [10, 20, 30, 40, 50, 60, 70]
desordenada = [40, 10, 70, 20, 60, 30, 50]
def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        print(f"inicio={inicio} meio={meio} fim={fim} -> olhando {lista[meio]}")
        if lista[meio] == alvo:
            return meio, comparacoes
        elif lista[meio] < alvo:
            inicio = meio +1
        else:
            fim = meio -1
    return -1, comparacoes
# COMPLETE: o alvo é maior, descarte a metade ESQUERDA

print(busca_binaria(ordenada, 60))
print(busca_binaria(desordenada, 60))