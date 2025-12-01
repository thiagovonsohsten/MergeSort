import time
import random

arrayLength = 1000000

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

print("Gerando vetor com " + str(arrayLength) + " elementos aleatórios...")
alist = [random.randint(1, 1000000) for _ in range(arrayLength)]

print("Iniciando ordenação...")
start = time.time()
mergeSort(alist)
end = time.time()

tempo_ms = (end - start) * 1000

print(f"Tempo de execução: {tempo_ms:.2f} milissegundos")

print("Verificando se está ordenado...")
ordenado = all(alist[i] <= alist[i+1] for i in range(len(alist)-1))
if ordenado:
    print("Vetor ordenado corretamente!")
else:
    print("Erro na ordenação!")