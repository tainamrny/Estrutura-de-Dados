def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1

lista = [10, 32, 55, 4]
alvo = 55
print(busca_linear(lista, alvo))