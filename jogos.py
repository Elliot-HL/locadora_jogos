from persistencia import salvar_jogos

plataformas = ["XBOX", "PC", "NINTENDO", "PLAYSTAION"]
jogos = []

def cadastrar_jogo(titulo, plataforma, genero, valor):
    jogo = {'titulo': titulo, 'plataforma': plataforma, 'genero': genero, 'valor': valor}
    jogos.append(jogo)
    salvar_jogos(jogos)
