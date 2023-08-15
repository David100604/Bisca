from jogo import Jogo

jogo1 = Jogo()

jogo1.CriarJogo(4)
jogo1.embaralhar()
jogo1.Cortar()
jogo1.distribuir_cartas(3)
jogo1.MostrarCartas()
jogo1.CriarDuplas()
jogo1.DefinirComeco()
for jogador in jogo1.jogadores:
    print(jogador.nome)
    print(jogador.vez)



