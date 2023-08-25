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
        self.corte = None
        self.ordem = []
        self.mesa = []
        self.naipesJogados = []
        self.valoresJogados = []
        self.valorMandante = -4
        self.chaveCartas = {}

    def CriarJogo(self, num_jogadores):
        if not self.jogadores:
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
        self.idCortador = random.randint(1, len(self.jogadores))
        for jogador in self.jogadores:
            if jogador.id == self.idCortador - 1:
                num = int(input(f"{jogador.nome}, insira um número de 0 a 39: "))
        if num < 0 or num >= self.baralho.qtdeCartas:
            print("Número fora do intervalo válido.")
            return

        self.cartaCortada = self.cartas.pop(num)
        print("Carta cortada:", self.cartaCortada)
        if self.cartaCortada in self.biscas:
            if '♥' in self.cartaCortada:
                self.corte = "♦"
                print('corte:', self.corte)
            elif '♦' in self.cartaCortada:
                self.corte = '♥'
                print('corte:', self.corte)
            elif '♣' in self.cartaCortada:
                self.corte = '♠'
                print('corte:', self.corte)
            elif '♠' in self.cartaCortada:
                self.corte = '♣'
                print('corte:', self.corte)
        else:
            self.corte = self.cartaCortada[1:]
            print('corte:', self.corte)

        return self.cartaCortada, self.idCortador

    def distribuir_cartas(self, cartas_por_jogador):

        for i in range(cartas_por_jogador):
            for jogador in self.jogadores:
                if len(self.cartas) > 0:
                    carta = self.cartas.pop()
                    jogador.mao.append(carta)

        if len(self.cartas) == 0 and self.cartaCortada is not None:
            self.jogadores[-1].mao.append(self.cartaCortada)

        return self.jogadores

    def DefinirComeco(self):
        ordem_de_jogada = [1, 2, 3, 4]
        indice_cortador = ordem_de_jogada.index(self.idCortador) + 2
        ordem = ordem_de_jogada[indice_cortador:] + ordem_de_jogada[:indice_cortador]
        for jogador in self.jogadores:
            jogador.vez = ordem[jogador.id]
        return ordem

    def Terminou(self):
        for jogador in self.jogadores:
            if len(jogador.mao) > 0:
                return False
        return True

    def Comecar(self):
        self.CriarJogo(4)
        self.embaralhar()

        self.Cortar()
        self.distribuir_cartas(3)
        self.CriarDuplas()
        self.ordem = self.DefinirComeco()

        while not self.Terminou():
            self.Rodada()
            print(self.mesa)
            if len(self.cartas) > 0:
                self.distribuir_cartas(1)

    def Rodada(self):
        self.mesa = []
        self.naipesJogados = []
        self.valoresJogados = []

        for i in self.ordem:
            jogador = self.jogadores[i - 1]
            carta_jogada = jogador.Jogar()
            carta = carta_jogada[:1]
            self.mesa.append(carta_jogada)
            naipeCarta = carta_jogada[1:]
            self.naipesJogados.append(naipeCarta)
            valor = self.baralho.valor[carta]
            self.valoresJogados.append(valor)

        self.DefinirNaipeGanhador()


    def DefinirNaipeGanhador(self):
        cartaMandante = None

        for i, c in enumerate(self.mesa):
            naipeCarta = c[1:]

            if self.corte in self.naipesJogados:
                naipeMandante = self.corte
                cartaMandante = c
                self.valorMandante = self.valoresJogados[i]
            else:
                naipeMandante = self.naipesJogados[0]


        valorMandante = self.valoresJogados[0]
        if cartaMandante is None:
            cartaMandante = self.mesa[0]

        ganhadoras = []

        for i, v in enumerate(self.valoresJogados):
                if self.naipesJogados[i] == naipeMandante:
                    ganhadoras.append(v)

        valorMandante = max(ganhadoras)
        self.inverterChaves()
        cartaMandante = self.chaveCartas[valorMandante]
        print(cartaMandante + naipeMandante)

    def inverterChaves(self):

        for chave, valor in self.baralho.valor.items():
            self.chaveCartas[valor] = chave







