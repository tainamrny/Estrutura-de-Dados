def busca_binaria(lista, item):
    baixo = 0
    alto = len(lista) -1
    while baixo <= alto:
        meio = (baixo + alto)//2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio -1
        else:
            baixo = meio +1
        return None
    
minha_lista =[10, 20, 30, 40, 80]
print(busca_binaria(minha_lista, 40))
print(busca_binaria(minha_lista, -1))