class Jogador:
    def __init__(self, nome):
        self.id = 1
        self.dupla = ""
        self.vez = 0
        self.nome = nome
        self.mao = []

    def Jogar(self):
        print(f"{self.nome}, é a sua vez de jogar.")
        print("Suas cartas:", self.mao)

        carta_jogada = input("Escolha uma carta para jogar (digite o índice da carta na sua mão): ")

        try:
            carta_jogada_index = int(carta_jogada) - 1
            carta_jogada = self.mao[carta_jogada_index]
            self.mao.pop(carta_jogada_index)
            print(f"{self.nome} jogou a carta: {carta_jogada}")
            return carta_jogada
        except (ValueError, IndexError):
            print("Opção inválida. Tente novamente.")
            return None

