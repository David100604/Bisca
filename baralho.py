from jogador import Jogador
import random

class Baralho():
    def __init__(self):
        self.cartasC = ['2♥', '3♥', '4♥', '5♥', '6♥', 'Q♥', 'J♥', 'K♥', '7♥', 'A♥']
        self.cartasP = ['2♣', '3♣', '4♣', '5♣', '6♣', 'Q♣', 'J♣', 'K♣', '7♣', 'A♣']
        self.cartasO = ['2♦', '3♦', '4♦', '5♦', '6♦', 'Q♦', 'J♦', 'K♦', '7♦', 'A♦']
        self.cartasE = ['2♠', '3♠', '4♠', '5♠', '6♠', 'Q♠', 'J♠', 'K♠', '7♠', 'A♠']
        self.cartas = self.cartasC + self.cartasP + self.cartasE + self.cartasO
        self.qtdeCartas = 40
        self.biscas = ['7♠', 'A♠', '7♦', 'A♦', '7♣', 'A♣', '7♥', 'A♥']
        self.valor = {"2": -3,
                      "3": -2,
                      "4": -1,
                      "5": 0,
                      "6": 1,
                      "Q": 2,
                      "J": 3,
                      "K": 4,
                      "7": 10,
                      "A": 11
                      }

    def consultar(self):
        print(self.cartas)

    def embaralhar(self):
        random.shuffle(self.cartas)

    def MostrarCartas(self):
        for jogador in self.jogadores:
            print(f"{jogador.nome}: {jogador.mao}")

