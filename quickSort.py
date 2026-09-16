#O primeiro elemento é o pivo


vetor =[0,10,5,2,3,1,4,6,7,8,9]

def quick_sort(vetor):
    if len(vetor) <= 1:
        return vetor
    else:
        pivo = vetor[0]
        menores = [x for x in vetor[1:] if x <= pivo]
        maiores = [x for x in vetor[1:] if x > pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)

print(quick_sort(vetor))