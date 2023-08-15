from jogador import Jogador
import random

class Baralho:
    def __init__(self):
        self.cartasC = ['2C', '3C', '4C', '5C', '6C', 'QC', 'JC', 'KC', '7C', 'AC']
        self.cartasP = ['2P', '3P', '4P', '5P', '6P', 'QP', 'JP', 'KP', '7P', 'AP']
        self.cartasO = ['2O', '3O', '4O', '5O', '6O', 'QO', 'JO', 'KO', '7O', 'AO']
        self.cartasE = ['2E', '3E', '4E', '5E', '6E', 'QE', 'JE', 'KE', '7E', 'AE']
        self.cartas = self.cartasC + self.cartasP + self.cartasE + self.cartasO
        self.qtdeCartas = 40

    def consultar(self):
        print(self.cartas)

    def embaralhar(self):
        random.shuffle(self.cartas)

    def MostrarCartas(self):
        for jogador in self.jogadores:
            print(f"{jogador.nome}: {jogador.mao}")


