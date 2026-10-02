def bubble_sort(lista):
    n = len(lista)
    trocas = 0
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
        # COMPLETE: troque lista[j] e lista[j+1] de lugar
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocas += 1
                trocou = True
        print(f"Fim da rodada {i + 1}: {lista}")
        if not trocou:
            print("Nenhuma troca: a lista já está ordenada!")
            break
    print(f"Total de trocas: {trocas}")
    return lista

print(bubble_sort([5, 3, 4, 1, 2]))
print(bubble_sort([1, 2, 3, 4, 5]))
