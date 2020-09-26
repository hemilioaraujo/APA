from geraVetor.vetor import VetorRandomico

from ordenacao.bubbleSort import bubbleSort
from ordenacao.heapSort import heapSort
from ordenacao.insertionSort import insertionSort
from ordenacao.quickSort import quickSort
from ordenacao.selectionSort import selectionSort
from ordenacao.shellSort import shellSort

import time

vetor_random = VetorRandomico().preenche_vetor(30)
metodos = {
    "BUBBLE": bubbleSort,
    "HEAP": heapSort,
    "INSERTION": insertionSort,
    "QUICK": quickSort,
    "SELECTION": selectionSort,
    "SHELL": shellSort
}


for i in metodos.keys():
    for j in range(3):
        inicio = time.time()
        ordenado, trocas = metodos[i](list(vetor_random))
        tempo = time.time() - inicio
        VetorRandomico.arquiva_resultados(j+1, vetor_random, ordenado, i, trocas, tempo)
