from geraVetor.vetor import VetorRandomico
from ordenacao.insertionSort import insertionSort
from ordenacao.selectionSort import selectionSort
from ordenacao.quickSort import quickSort
import timeit

vetor = VetorRandomico().preenche_vetor(5)
print(vetor)
# print(vetor.tamanho_vetor())

# print(insertionSort(vetor))
# print(selectionSort(vetor))
trocas = quickSort(vetor)
print(vetor, trocas)