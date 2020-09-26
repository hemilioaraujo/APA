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

    def cabecalho():
        file = open(f"resultados/dados_importantes.csv", "a")
        file.write("rodada;tipo;trocas;tempo\n")
        file.close()

    def arquiva_dados_importantes(rodada, tipo, trocas, tempo):
        file = open(f"resultados/dados_importantes.csv", "a")
        file.write(f"{rodada};{tipo};{trocas};{tempo}\n")
        file.close()

    def arquiva_resultados(rodada, vetor, ordenado, tipo, trocas, tempo):
        file = open(f"resultados/{tipo}" + ".txt", "a")
        file.write('**************************************************************************\n')
        file.write(f'                              {tipo} SORT [{rodada}]\n')
        file.write('**************************************************************************\n')

        file.write('**************************************************************************\n')
        file.write(f'                           VETOR DESORDENADO\n')
        file.write('**************************************************************************\n')
        for i in vetor:
            file.write(f"{str(i)} ")
        file.write("\n")

        file.write('**************************************************************************\n')
        file.write(f'                            VETOR ORDENADO\n')
        file.write('**************************************************************************\n')
        for i in ordenado:
            file.write(f"{str(i)} ")
        file.write("\n")
        
        file.write('**************************************************************************\n')
        file.write(f'                       TROCAS NECESSÁRIAS {trocas}\n')
        file.write('                       TEMPO NECESSÁRIO {:.9f}\n'.format(tempo))
        file.write('**************************************************************************\n')

        file.close()
        VetorRandomico.arquiva_dados_importantes(rodada, tipo, trocas, tempo)
