from baralho import Baralho
from jogador import Jogador
import random


class Jogo(Baralho):
    def __init__(self):
        super().__init__()
        self.baralho = Baralho()
        self.jogadores = []
        self.cartaCortada = None
        self.idCortador = 0

    def CriarJogo(self, num_jogadores):
        if self.jogadores == []:
            nomes = [input(f"Insira o nome do {i + 1}º jogador: ") for i in range(num_jogadores)]
            self.jogadores = [Jogador(nomes[i]) for i in range(num_jogadores)]
            for i, jogador in enumerate(self.jogadores):
                jogador.id = i

        return self.jogadores

    def CriarDuplas(self):
        for jogador in self.jogadores:
            if jogador.id == 0:
                for j in self.jogadores:
                    if j.id == 2:
                        jogador.dupla = j.nome
                        j.dupla = jogador.nome
            elif jogador.id == 1:
                for j in self.jogadores:
                    if j.id == 3:
                        jogador.dupla = j.nome
                        j.dupla = jogador.nome

    def Cortar(self):
        self.idCortador = random.randint(0, 3)
        for jogador in self.jogadores:
            if jogador.id == self.idCortador:
                num = int(input(f"{jogador.nome}, insira um número de 0 a 39: "))
        if num < 0 or num >= self.baralho.qtdeCartas:
            print("Número fora do intervalo válido.")
            return

        self.cartaCortada = self.cartas.pop(num)
        print("Carta cortada:", self.cartaCortada)
        return self.cartaCortada, self.idCortador

    def distribuir_cartas(self, cartas_por_jogador):

        for i in range(cartas_por_jogador):
            for jogador in self.jogadores:
                if len(self.cartas) > 0:
                    carta = self.cartas.pop()
                    jogador.mao.append(carta)

        if len(self.cartas) == 0 and self.cartaCortada is not None:
            self.jogadores[-1].mao.append(self.cartaCortada)  # Último jogador recebe a carta cortada

        return self.jogadores

    def DefinirComeco(self):
        ordem_de_jogada = [1, 2, 3, 4]
        indice_cortador = ordem_de_jogada.index(self.idCortador) + 1

        nova_ordem = ordem_de_jogada[indice_cortador:] + ordem_de_jogada[:indice_cortador]

        for jogador in self.jogadores:
            jogador.vez = nova_ordem[jogador.id - 1]


