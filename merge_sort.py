
    
#Primeiro a gente pega o array 



lista = [10000, 27, 43, 3, 9, 82, 10]
#segundo a gente precisa chamar a função merge_sort recursivamente para cada metade do array
def merge_sort(lista):
 #primeiro dividir a lista na metade 
 if len(lista) <= 1:
  return lista
 medida = len(lista)//2
 #pegar lado direito e lado esquerdo 
 esquerda = lista[:medida]
 direita = lista[medida:] 

 #chama a função recursiva para as duas metade
 esquerda_ordenada = merge_sort(esquerda)
 direita_ordenada = merge_sort(direita)
 return merge(esquerda_ordenada, direita_ordenada)




def merge(esquerda, direita):
    resultado=[]
    i=j=0
    while i < len(esquerda) and j < len(direita):
      if esquerda[i] < direita[j]:
        resultado.append(esquerda[i])
        i+=1
      else:
        resultado.append(direita[j])
        j+=1

    # Adicionar elementos restantes, se houver
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado

    
    
resultado_ordenado = merge_sort(lista)


print("Lista ordenada:", resultado_ordenado)