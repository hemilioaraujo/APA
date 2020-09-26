from geraVetor.vetor import VetorRandomico

from ordenacao.bubbleSort import bubbleSort
from ordenacao.heapSort import heapSort
from ordenacao.insertionSort import insertionSort
from ordenacao.quickSort import quickSort
from ordenacao.selectionSort import selectionSort
from ordenacao.shellSort import shellSort

import time

vetor_random = VetorRandomico().preenche_vetor(30000)

# bubble
for i  in range(5):
    inicio = time.time()
    ordenado, trocas = bubbleSort(list(vetor_random))
    tempo = time.time() - inicio
    VetorRandomico.arquiva_resultados(i+1, vetor_random, ordenado, "HEAP SORT", trocas, tempo, "bubble")