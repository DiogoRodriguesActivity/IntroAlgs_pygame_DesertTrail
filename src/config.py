WIDTH = 800
HEIGHT = 600
FPS = 60
GRAVITY = 0.6
MAP_WIDTH = 3200 # ampliando o mapa (3200 pixels - Diogo 14/06/2026)

Imagens = {
    "Imagem_fundo": "assets/imagens/FundoDesert.jpg",
    "engrenagem": "assets/imagens/Engrenagem.png",
    "entrada_templo": "assets/imagens/entrada_templo.png",
    "volume": "assets/imagens/volume.png",
    "mutado": "assets/imagens/mutado.png",

    "chao_topo_esq":  "assets/imagens/tiles/1.png",
    "chao_topo_mid":  "assets/imagens/tiles/2.png",
    "chao_topo_dir":  "assets/imagens/tiles/3.png",
    "chao_fill_esq":  "assets/imagens/tiles/4.png",
    "chao_fill_mid":  "assets/imagens/tiles/5.png",
    "chao_fill_dir":  "assets/imagens/tiles/6.png",
    "plat_esq":       "assets/imagens/tiles/14.png",
    "plat_mid":       "assets/imagens/tiles/15.png",
    "plat_dir":       "assets/imagens/tiles/16.png",
}

TILE_SIZE = 64

# Cores usadas no Jogo
SAND_YELLOW = (237, 201, 175)  # Cor de fundo do Deserto
DARK_YELLOW = (100, 101, 125)  # Hover
GREEN = (34, 139, 34)       
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)        
RED = (200, 30, 30)           

pontuacao = 0
vidas = 3
nome_jogador = ""  
fase_atual = 1                 # Nova variável para rastrear a fase atual (1, 2 ou 3)