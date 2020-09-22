from vetor import VetorRandomico
from ordenacao.insertionSort import insertionSort
import timeit

vetor = VetorRandomico().preenche_vetor(30)
print(vetor)
# print(vetor.tamanho_vetor())

print(insertionSort(vetor))