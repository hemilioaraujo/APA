from random import randint


class VetorRandomico:
    def __init__(self):
        self.vetor = []

    def preenche_vetor(self, n):
        for i in range(n):
            self.vetor.append(randint(10000, 99999))

    def print_vetor(self):
        for i in self.vetor:
            print(i)

    def tamanho_vetor(self):
        return len(self.vetor)
