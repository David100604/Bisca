class Jogador():
    def __init__(self, nome):
        self.id = 1
        self.dupla = None
        self.vez = 0
        self.nome = nome
        self.mao = []
        self.monte = []
        self.pontos = 0
        self.pontodDupla = 0
        self.corte = None
        self.cartaJogada = None
        self.carta = None
        self.naipe = None
        self.cartasJogadas = []
        self.sete = None
        self.a = None
        self.qtdeJogadores = 0

    def Jogar(self):
        print(f"{self.nome}, é a sua vez de jogar.")
        print("Suas cartas:", self.mao)

        self.cartaJogada = input("Escolha uma carta para jogar (digite o índice da carta na sua mão): ")

        try:
            carta_jogada_index = int(self.cartaJogada) - 1
            self.cartaJogada = self.mao[carta_jogada_index]
            self.naipe = self.cartaJogada[1:]
            self.carta = self.cartaJogada[:1]
            print(self.carta)
            print(self.vez)

            while self.cartaJogada == self.sete:
                if self.qtdeJogadores == 4:
                    if self.vez == 4:
                        if self.a not in self.mao:
                            self.cartaJogada = input("Você não pode jogar está carta, escolha outra: ")
                            carta_jogada_index = int(self.cartaJogada) - 1
                            self.cartaJogada = self.mao[carta_jogada_index]
                        else:
                            self.cartaJogada = self.sete
                            break
                    else:
                        self.cartaJogada = self.sete
                        break
                elif self.qtdeJogadores == 3:
                    if self.vez == 3:
                        if self.a not in self.mao:
                            self.cartaJogada = input("Você não pode jogar está carta, escolha outra: ")
                            carta_jogada_index = int(self.cartaJogada) - 1
                            self.cartaJogada = self.mao[carta_jogada_index]
                        else:
                            self.cartaJogada = self.sete
                            break
                    else:
                        self.cartaJogada = self.sete
                        break
                elif self.qtdeJogadores == 2:
                    if self.vez == 2:
                        if self.a not in self.mao:
                            self.cartaJogada = input("Você não pode jogar está carta, escolha outra: ")
                            carta_jogada_index = int(self.cartaJogada) - 1
                            self.cartaJogada = self.mao[carta_jogada_index]
                        else:
                            self.cartaJogada = self.sete
                            break
                    else:
                        self.cartaJogada = self.sete
                        break
            else:
                while self.cartaJogada == self.a:
                    if self.sete not in self.cartasJogadas:
                        if self.sete not in self.mao:
                            self.cartaJogada = input("Você não pode jogar o Às do corte antes do 7, escolha outra: ")
                            carta_jogada_index = int(self.cartaJogada) - 1
                            self.cartaJogada = self.mao[carta_jogada_index]
                        else:
                            self.cartaJogada = self.a
                            break
                    else:
                        self.cartaJogada = self.a
                        break

            self.mao.pop(carta_jogada_index)
            return self.cartaJogada
        except (ValueError, IndexError):
            print("Opção inválida. Tente novamente.")
            return None


