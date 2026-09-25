#velocidade o(n) se ao rodar não acontecer nenhuma troca
#normalmente é o(n²)
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i -1):  #faz o j percorrer a lista pra direita
            if lista[j] > lista[j+1]: #se o atual for maior que o vizinho
                lista[j], lista[j+1] = lista[j+1], lista[j] #troca de lugar
    return lista

numeros = [3, 4, 9, 6]
print(bubble_sort(numeros))