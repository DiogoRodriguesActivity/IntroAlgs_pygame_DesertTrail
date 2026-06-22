import pygame
import config
from button import criar_botao
from funcoes import desenhar_texto

def exibir_menu(tela, fonte_titulo, fonte_menu, acao_start, acao_select):
    # Titulo
    desenhar_texto(tela, "MENU PRINCIPAL", fonte_titulo, config.COR_DESTAQUE, config.LARGURA // 2, 120)
    
    # Botoes
    criar_botao(tela, "START", fonte_menu, config.LARGURA // 2 - 100, 250, 200, 60, acao_start)
    criar_botao(tela, "SELECT", fonte_menu, config.LARGURA // 2 - 100, 350, 200, 60, acao_select)