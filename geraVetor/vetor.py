from random import randint


class VetorRandomico:
    def __init__(self):
        self.vetor = []

    def preenche_vetor(self, n):
        for i in range(n):
            self.vetor.append(randint(10000, 99999))
            arr = self.vetor
        return arr

    def print_vetor(self):
        for i in self.vetor:
            print(i)

    def tamanho_vetor(self):
        return len(self.vetor)

    def print_resultados(vetor, ordenado, tipo, trocas):
        print('\n**************************************************************************')
        print(f'                              {tipo}')
        print('**************************************************************************\n')

        print('\n**************************************************************************')
        print(f'                           VETOR DESORDENADO')
        print('**************************************************************************\n')
        print(vetor)

        print('\n**************************************************************************')
        print(f'                            VETOR ORDENADO')
        print('**************************************************************************\n')
        print(ordenado)

        print('\n**************************************************************************')
        print(f'                       TROCAS NECESSÁRIAS {trocas}')
        print('**************************************************************************\n')

