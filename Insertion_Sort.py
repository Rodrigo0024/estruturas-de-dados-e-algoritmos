def insertion_sort(ordenacao):
    # Começamos do segundo elemento (índice 1), assumindo que o primeiro (índice 0) já está "ordenado"
    for i in range(1, len(ordenacao)):
        posicao = ordenacao[i]  
        j = i - 1  
        #Comparar o elemto da esquerda com o da direita
        if ordenacao[j] > posicao:
            # Move os elementos da parte ordenada que são maiores que a posicao para a frente
            while j >= 0 and ordenacao[j] > posicao:
                ordenacao[j + 1] = ordenacao[j]
                j -= 1
            ordenacao[j + 1] = posicao   
        
       
        
    return ordenacao

# Testando o algoritmo:
lista = [12, 11, 13, 5, 6]
print("Lista original:", lista)

insertion_sort(lista)
print("Lista ordenada:", lista)