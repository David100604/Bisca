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

    def Jogar(self):
        print(f"{self.nome}, é a sua vez de jogar.")
        print("Suas cartas:", self.mao)

        self.cartaJogada = int(input("Escolha uma carta para jogar (digite o índice da carta na sua mão): "))

        while self.cartaJogada > len(self.mao):
            input("Escolha uma carta para jogar (Insira um número de 1 a {}): ".format(len(self.mao)))

        try:
            carta_jogada_index = self.cartaJogada - 1
            self.cartaJogada = self.mao[carta_jogada_index]
            self.naipe = self.cartaJogada[1:]
            self.carta = self.cartaJogada[:1]
            print(self.carta)
            print(self.vez)

            while self.cartaJogada == self.sete:
                if self.a in self.mao:
                    break
                else:
                    if self.vez == 4:
                        self.cartaJogada = input("Você não pode jogar está carta, escolha outra: ")
                        carta_jogada_index = int(self.cartaJogada) - 1
                        self.cartaJogada = self.mao[carta_jogada_index]
                    else:
                        self.cartaJogada = self.sete
                        break
            else:
                while self.cartaJogada == self.a:
                    if self.sete in self.mao:
                        break
                    else:
                        if self.sete not in self.cartasJogadas:
                            self.cartaJogada = input("Você não pode jogar o Às do corte antes do 7, escolha outra: ")
                            carta_jogada_index = int(self.cartaJogada) - 1
                            self.cartaJogada = self.mao[carta_jogada_index]
                        else:
                            self.cartaJogada = self.a
                            break

            self.mao.pop(carta_jogada_index)
            return self.cartaJogada
        except (ValueError, IndexError):
            print("Opção inválida. Tente novamente.")
            return None

