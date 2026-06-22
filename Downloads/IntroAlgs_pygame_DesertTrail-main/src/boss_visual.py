import math
from pathlib import Path

import pygame


# Paleta da arena da Esfinge
CEU_TOPO = (34, 24, 63)
CEU_BASE = (181, 78, 64)
AREIA_ESCURO = (119, 63, 50)
AREIA = (222, 159, 75)
OURO = (240, 190, 75)
OURO_CLARO = (255, 224, 137)
PERGAMINHO = (255, 238, 190)
MARROM = (64, 39, 35)
VERMELHO = (205, 57, 54)
_SPRITE_ESFINGE = None


def _texto_centralizado(tela, texto, fonte, cor, centro_x, y):
    imagem = fonte.render(texto, True, cor)
    tela.blit(imagem, imagem.get_rect(midtop=(centro_x, y)))


def _linhas(texto, fonte, largura_maxima):
    palavras = texto.split()
    linhas, linha = [], ""
    for palavra in palavras:
        tentativa = f"{linha} {palavra}".strip()
        if fonte.size(tentativa)[0] <= largura_maxima:
            linha = tentativa
        else:
            if linha:
                linhas.append(linha)
            linha = palavra
    if linha:
        linhas.append(linha)
    return linhas


def _desenhar_fundo(tela):
    largura, altura = tela.get_size()
    # Degrade do anoitecer.
    for y in range(altura):
        proporcao = y / altura
        cor = tuple(
            int(CEU_TOPO[i] + (CEU_BASE[i] - CEU_TOPO[i]) * proporcao)
            for i in range(3)
        )
        pygame.draw.line(tela, cor, (0, y), (largura, y))

    pygame.draw.circle(tela, (255, 218, 143), (675, 105), 45)
    pygame.draw.circle(tela, (255, 232, 174), (675, 105), 34)

    # Piramides e dunas em silhueta.
    pygame.draw.polygon(tela, (86, 48, 57), [(20, 360), (175, 145), (330, 360)])
    pygame.draw.polygon(tela, (67, 40, 52), [(480, 350), (590, 205), (700, 350)])
    pygame.draw.polygon(tela, (142, 77, 58), [(175, 145), (330, 360), (225, 360)])
    pygame.draw.polygon(tela, (112, 62, 57), [(590, 205), (700, 350), (625, 350)])
    pygame.draw.ellipse(tela, AREIA_ESCURO, (-100, 325, 600, 230))
    pygame.draw.ellipse(tela, (145, 82, 53), (310, 335, 650, 230))
    pygame.draw.rect(tela, (91, 53, 43), (0, 475, largura, altura - 475))


def _desenhar_esfinge(tela):
    global _SPRITE_ESFINGE
    if _SPRITE_ESFINGE is None:
        caminho = Path(__file__).resolve().parents[1] / "assets" / "imagens" / "esfinge_pixel.png"
        imagem = pygame.image.load(str(caminho))
        recorte = imagem.get_bounding_rect(min_alpha=10)
        proporcao = recorte.height / recorte.width
        _SPRITE_ESFINGE = pygame.transform.scale(
            imagem.subsurface(recorte), (230, int(230 * proporcao))
        )

    sombra = pygame.Rect(12, 425, 215, 25)
    pygame.draw.ellipse(tela, (58, 35, 31), sombra)
    tela.blit(_SPRITE_ESFINGE, (4, 250))
    return

    # Uma Esfinge estilizada, feita apenas com formas para não exigir novos assets.
    halo = pygame.Surface((238, 285), pygame.SRCALPHA)
    pygame.draw.ellipse(halo, (255, 194, 79, 42), (3, 2, 226, 268))
    tela.blit(halo, (0, 172))
    pygame.draw.ellipse(tela, (52, 32, 35), (18, 256, 202, 98))
    pygame.draw.ellipse(tela, (151, 86, 42), (24, 262, 190, 85))
    pygame.draw.rect(tela, (52, 32, 35), (36, 305, 45, 128), border_radius=14)
    pygame.draw.rect(tela, (52, 32, 35), (151, 305, 45, 128), border_radius=14)
    pygame.draw.rect(tela, (151, 86, 42), (41, 310, 35, 118), border_radius=12)
    pygame.draw.rect(tela, (151, 86, 42), (156, 310, 35, 118), border_radius=12)
    pygame.draw.polygon(tela, OURO, [(73, 285), (115, 211), (157, 285)])
    pygame.draw.circle(tela, (52, 32, 35), (115, 242), 40)
    pygame.draw.circle(tela, (221, 158, 72), (115, 242), 35)
    pygame.draw.polygon(tela, (54, 39, 57), [(79, 221), (115, 183), (151, 221), (142, 273), (88, 273)])
    pygame.draw.rect(tela, OURO, (83, 207, 64, 12), border_radius=4)
    pygame.draw.polygon(tela, OURO_CLARO, [(115, 217), (108, 250), (122, 250)])
    pygame.draw.circle(tela, OURO_CLARO, (101, 237), 5)
    pygame.draw.circle(tela, OURO_CLARO, (129, 237), 5)
    pygame.draw.circle(tela, (34, 23, 29), (101, 237), 2)
    pygame.draw.circle(tela, (34, 23, 29), (129, 237), 2)
    pygame.draw.arc(tela, (76, 39, 30), (103, 244, 24, 16), math.pi * .1, math.pi * .9, 2)
    pygame.draw.polygon(tela, (151, 86, 42), [(26, 282), (7, 228), (45, 267)])
    pygame.draw.line(tela, OURO_CLARO, (42, 315), (42, 402), 2)
    pygame.draw.line(tela, OURO_CLARO, (190, 315), (190, 402), 2)


def desenhar_boss(tela, pergunta, fase, vidas, pontuacao, nome_jogador):
    largura, _ = tela.get_size()
    _desenhar_fundo(tela)
    _desenhar_esfinge(tela)

    fonte_titulo = pygame.font.SysFont("georgia", 27, bold=True)
    fonte_subtitulo = pygame.font.SysFont("georgia", 18, italic=True)
    fonte_pergunta = pygame.font.SysFont("georgia", 22, bold=True)
    fonte_opcao = pygame.font.SysFont("arial", 19, bold=True)
    fonte_hud = pygame.font.SysFont("arial", 17, bold=True)

    # Faixa superior.
    pygame.draw.rect(tela, (38, 27, 43), (0, 0, largura, 69))
    pygame.draw.line(tela, OURO, (0, 68), (largura, 68), 3)
    _texto_centralizado(tela, f"DESAFIO DA ESFINGE  •  FASE {fase}", fonte_titulo, OURO_CLARO, largura // 2, 8)
    _texto_centralizado(tela, "Decifra-me ou devoro-te!", fonte_subtitulo, (235, 208, 172), largura // 2, 42)

    # HUD de jogador e vidas.
    painel_hud = pygame.Rect(18, 82, 205, 57)
    pygame.draw.rect(tela, (35, 27, 38), painel_hud, border_radius=10)
    pygame.draw.rect(tela, OURO, painel_hud, 2, border_radius=10)
    tela.blit(fonte_hud.render(nome_jogador or "Herói", True, (255, 239, 202)), (31, 91))
    tela.blit(fonte_hud.render(f"Pontos: {pontuacao}", True, (220, 188, 126)), (31, 113))
    for indice in range(3):
        cor = VERMELHO if indice < vidas else (83, 67, 72)
        x = 158 + indice * 20
        pygame.draw.circle(tela, cor, (x, 105), 7)
        pygame.draw.circle(tela, cor, (x + 9, 105), 7)
        pygame.draw.polygon(tela, cor, [(x - 7, 108), (x + 16, 108), (x + 5, 122)])

    # Pergaminho da pergunta.
    painel = pygame.Rect(245, 91, 525, 155)
    sombra = painel.move(6, 7)
    pygame.draw.rect(tela, (45, 29, 31), sombra, border_radius=14)
    pygame.draw.rect(tela, PERGAMINHO, painel, border_radius=14)
    pygame.draw.rect(tela, OURO, painel, 4, border_radius=14)
    _texto_centralizado(tela, "O ENIGMA", fonte_subtitulo, (139, 79, 39), painel.centerx, 105)

    linhas = _linhas(pergunta["pergunta"], fonte_pergunta, painel.width - 48)
    inicio_y = 142 - max(0, len(linhas) - 1) * 10
    for indice, linha in enumerate(linhas):
        _texto_centralizado(tela, linha, fonte_pergunta, MARROM, painel.centerx, inicio_y + indice * 29)

    # Cartões das alternativas em duas colunas.
    letras = ("A", "B", "C", "D")
    for indice, opcao in enumerate(pergunta["opcoes"]):
        coluna, linha = indice % 2, indice // 2
        rect = pygame.Rect(245 + coluna * 267, 274 + linha * 84, 250, 66)
        pygame.draw.rect(tela, (43, 31, 43), rect.move(4, 5), border_radius=11)
        pygame.draw.rect(tela, (255, 235, 185), rect, border_radius=11)
        pygame.draw.rect(tela, (191, 130, 52), rect, 3, border_radius=11)
        pygame.draw.circle(tela, (125, 70, 42), (rect.x + 30, rect.centery), 19)
        letra = fonte_opcao.render(letras[indice], True, (255, 229, 165))
        tela.blit(letra, letra.get_rect(center=(rect.x + 30, rect.centery)))
        texto_opcao = opcao.split(")", 1)[-1].strip()
        imagem = fonte_opcao.render(texto_opcao, True, MARROM)
        tela.blit(imagem, (rect.x + 58, rect.centery - imagem.get_height() // 2))

    instrucao = pygame.Rect(245, 461, 525, 43)
    pygame.draw.rect(tela, (35, 27, 38), instrucao, border_radius=9)
    pygame.draw.rect(tela, OURO, instrucao, 2, border_radius=9)
    _texto_centralizado(tela, "Pressione  A, B, C  ou  D  para responder", fonte_hud, (255, 228, 168), instrucao.centerx, 472)

    _texto_centralizado(tela, "Escolha com sabedoria, viajante...", fonte_subtitulo, (238, 199, 137), largura // 2, 548)
