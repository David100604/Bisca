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
        self.winnerId = 1
        self.ordem = []


    def CriarJogo(self, num_jogadores):
        if num_jogadores > 4 or num_jogadores < 2:
            print("Não é possível criar o jogo com ", num_jogadores," jogadores, escolha entre 2 e 4.")
            exit()

        if num_jogadores == 3:
            cartaRemovida = "2♠"
            self.cartas.remove(cartaRemovida)
            self.qtdeCartas = 39

        if not self.jogadores:
            nomes = [input(f"Insira o nome do {i + 1}º jogador: ") for i in range(num_jogadores)]
            self.jogadores = [Jogador(nomes[i]) for i in range(num_jogadores)]
        for i, jogador in enumerate(self.jogadores):
            jogador.id = i
            jogador.qtdeJogadores = num_jogadores

        return self.jogadores

    def CriarDuplas(self):

        if len(self.jogadores) == 4:
            for jogador in self.jogadores:
                if jogador.id == 0:
                    for j in self.jogadores:
                        if j.id == 2:
                            jogador.dupla = j
                            j.dupla = jogador
                elif jogador.id == 1:
                    for j in self.jogadores:
                        if j.id == 3:
                            jogador.dupla = j
                            j.dupla = jogador
        else:
            pass

    def Cortar(self):
        self.idCortador = random.randint(1, len(self.jogadores))
        for jogador in self.jogadores:
            if jogador.id == self.idCortador - 1:
                num = int(input(f"{jogador.nome}, insira um número de 0 a {len(self.cartas) -1}: "))
        if num < 0 or num >= self.baralho.qtdeCartas:
            print("Número fora do intervalo válido.")
            return

        self.cartaCortada = self.cartas.pop(num)
        print("Carta cortada:", self.cartaCortada)
        if self.cartaCortada in self.biscas:
            if '♥' in self.cartaCortada:
                self.corte = "♦"
                jogador.corte = "♦"
            elif '♦' in self.cartaCortada:
                self.corte = '♥'
                jogador.corte = '♥'
            elif '♣' in self.cartaCortada:
                self.corte = '♠'
                jogador.corte = '♠'
            elif '♠' in self.cartaCortada:
                self.corte = '♣'
                jogador.corte = '♣'
        else:
            self.corte = self.cartaCortada[1:]
            jogador.corte = self.cartaCortada[1:]

        for jogador in self.jogadores:
            jogador.sete = '7' + self.corte
            jogador.a = 'A' + self.corte

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
        if len(self.jogadores) == 4:
            ordem_de_jogada = [1, 2, 3, 4]
            indice_cortador = ordem_de_jogada.index(self.idCortador) + 2
            self.ordem = ordem_de_jogada[indice_cortador:] + ordem_de_jogada[:indice_cortador]
            for jogador in self.jogadores:
                jogador.vez = self.ordem[jogador.id]
            return self.ordem
        elif len(self.jogadores) == 2:
            ordem_de_jogada = [1, 2]
            indice_cortador = ordem_de_jogada.index(self.idCortador) + 2
            self.ordem = ordem_de_jogada[indice_cortador:] + ordem_de_jogada[:indice_cortador]
            for jogador in self.jogadores:
                jogador.vez = self.ordem[jogador.id]
            return self.ordem
        elif len(self.jogadores) == 3:
            ordem_de_jogada = [1, 2, 3]
            indice_cortador = ordem_de_jogada.index(self.idCortador) + 2
            self.ordem = ordem_de_jogada[indice_cortador:] + ordem_de_jogada[:indice_cortador]
            for jogador in self.jogadores:
                jogador.vez = self.ordem[jogador.id]
            return self.ordem

    def Terminou(self):
        for jogador in self.jogadores:
            if len(jogador.mao) > 0:
                return False
        return True


    def Rodada(self):
        self.mesa = []
        self.naipesJogados = []
        self.valoresJogados = []

        for n, i in enumerate(self.ordem):
            print("Corte: ", self.corte)
            print("Mesa: ", self.mesa)
            jogador = self.jogadores[i - 1]
            jogador.vez  = n + 1
            carta_jogada = jogador.Jogar()
            carta = carta_jogada[:1]
            self.mesa.append(carta_jogada)
            print('\n' *130)
            naipeCarta = carta_jogada[1:]
            self.naipesJogados.append(naipeCarta)
            valor = self.baralho.valor[carta]
            self.valoresJogados.append(valor)
            for j in self.jogadores:
                j.cartasJogadas.append(carta_jogada)

        self.DefinirCartaGanhadora()
        self.DefinirNovoComeco()


    def DefinirCartaGanhadora(self):
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
        carta = self.chaveCartas[valorMandante]
        cartaMandante = carta + naipeMandante
        print(cartaMandante)

        for i, c in enumerate(self.mesa):
            if c == cartaMandante:
                for x, j in enumerate(self.jogadores):
                    if j.vez == i + 1:
                        j.monte.append(self.mesa)
                        self.winnerId = j.id + 1
                        print(j.nome, " ganhou a rodada com a carta: ", c)

        return  self.winnerId

    def DefinirNovoComeco(self):
            ordem_de_jogada = self.ordem
            winner_index = ordem_de_jogada.index(self.winnerId)
            self.ordem = ordem_de_jogada[winner_index:] + ordem_de_jogada[:winner_index]

            for jogador in self.jogadores:
                jogador.vez = self.ordem[jogador.id]

            return self.ordem

    def inverterChaves(self):

        for chave, valor in self.baralho.valor.items():
            self.chaveCartas[valor] = chave


    def ContarPontos(self):

        for jogador in self.jogadores:
            for lista in jogador.monte:
                for c in lista:
                    carta = c[:1]
                    if carta == "Q":
                        jogador.pontos += 2
                    elif carta == "J":
                        jogador.pontos += 3
                    elif carta == "K":
                        jogador.pontos += 4
                    elif carta == "7":
                        jogador.pontos += 10
                    elif carta == "A":
                        jogador.pontos += 11

        if len(self.jogadores) == 4:
            for jogador in self.jogadores:
                jogador.pontosDupla = jogador.pontos + jogador.dupla.pontos


    def ExibirGanhador(self):
        ganhadores = []
        perdedores = []
        ganhador = None
        perdedor = None

        for jogador in self.jogadores:
            if len(self.jogadores) == 4:
                if jogador.pontosDupla > 60:
                    ganhadores.append(jogador)
                elif jogador.pontosDupla < 60:
                    perdedores.append(jogador)
                elif jogador.pontosDupla == 60:
                    print("EMPATE")

            elif len(self.jogadores) == 2 or len(self.jogadores) == 3:
                if jogador.pontos > 60:
                    print("O jogador ", jogador.nome, " ganhou com ", jogador.pontos, " pontos.")
                elif jogador.pontos < 60:
                    print("O jogador ", jogador.nome, " perdeu com ", jogador.pontos, " pontos.")
                elif jogador.pontos == 60:
                    print("EMPATE")

        if len(self.jogadores) == 4:
            ganhador1 = ganhadores[0].nome
            ganhador2 = ganhadores[1].nome
            print("Os jogadores ", ganhador1, ganhador2, " ganharam com ", ganhadores[0].pontosDupla, " pontos.")

            perdedor1 = perdedores[0].nome
            perdedor2 = perdedores[1].nome
            print("Os jogadores ", perdedor1, perdedor2, " perderam com ", perdedores[0].pontosDupla, " pontos.")


    def Comecar(self):
        self.CriarJogo(3)
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

        self.ContarPontos()
        self.ExibirGanhador()



