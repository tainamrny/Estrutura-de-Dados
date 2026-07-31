def cria_lista ():
    #a variavel números vai para a memória stack e os dados da lista vai para o heap
    numeros = [1, 2 , 3]
    return numeros

resultado = cria_lista()
# a função acabou mais ainda existe no heap
print(resultado)