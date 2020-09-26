from geraVetor.vetor import VetorRandomico

from ordenacao.bubbleSort import bubbleSort
from ordenacao.heapSort import heapSort
from ordenacao.insertionSort import insertionSort
from ordenacao.quickSort import quickSort
from ordenacao.selectionSort import selectionSort
from ordenacao.shellSort import shellSort

import time

qtd_numeros = 30000
vetor_random = []
vetor_random.append(VetorRandomico().preenche_vetor(qtd_numeros))
vetor_random.append(VetorRandomico().preenche_vetor(qtd_numeros))
vetor_random.append(VetorRandomico().preenche_vetor(qtd_numeros))

metodos = {
    "BUBBLE": bubbleSort,
    "HEAP": heapSort,
    "INSERTION": insertionSort,
    "QUICK": quickSort,
    "SELECTION": selectionSort,
    "SHELL": shellSort
}

VetorRandomico.cabecalho()

for i in metodos.keys():
    for j in range(3):
        inicio = time.time()
        ordenado, trocas = metodos[i](list(vetor_random[j]))
        tempo = time.time() - inicio
        VetorRandomico.arquiva_resultados(j+1, vetor_random[j], ordenado, i, trocas, tempo)
