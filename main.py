from vetor import VetorRandomico
from ordenacao.insertionSort import insertionSort
from ordenacao.selectionSort import selectionSort
import timeit

vetor = VetorRandomico().preenche_vetor(30)
print(vetor)
# print(vetor.tamanho_vetor())

# print(insertionSort(vetor))
print(selectionSort(vetor))