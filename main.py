import pygame
import sys
import os
import random

from src.button import Button, botoes_config
from src.config import *
import src.config as config
from src.player import Player
from src.fase import Fase
from src.funcoes import check_colisoes, draw_text
from src.perguntas import PERGUNTAS_POR_FASE
from src.boss_visual import desenhar_boss


class Jogo(object):

    def main():
        pygame.init()

        # Fonte do Jogo
        font = pygame.font.Font(None, 36)

        som_ativo = True

        try:
            pygame.mixer.init()
        except pygame.error as e:
            print(f"Audio desabilitado: {e}")
            som_ativo = False
        if som_ativo:
            # Area para quem for adicionar as musicas e efeitos sonoros
            pygame.mixer.music.load("assets/sons/purrsahfef-8-bit-space-123218.mp3")
            pygame.mixer.music.set_volume(0.3)  # volume de 0.0 a 1.0
            pygame.mixer.music.play(-1)         # -1 = loop infinito

            # Efeitos Sonoros
            acerto = pygame.mixer.Sound("assets/sons/win.mp3")
            erro = pygame.mixer.Sound("assets/sons/gameover.mp3")
            
            # Canal dedicado para os efeitos (para sabermos quando terminam)
            canal_efeitos = pygame.mixer.Channel(0)

        # Pontuação de cada pergunta da esfinge: 1ª, 2ª e 3ª (a 3ª é só bônus)
        PONTOS_PERGUNTA = [50, 50, 100]
        BONUS_DUPLA = 100  # bônus extra por acertar a 1ª E a 2ª pergunta

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Desert Trail - A Jornada do Explorador")
        clock = pygame.time.Clock()

        # Resolvendo o problema do caminho
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        
        # Carrega a imagem do menu direto e trata as barras para o Windows
        caminho_menu = os.path.join(BASE_DIR, "assets", "imagens", "telamenu.png")
        Fundo_Menu_Novo = pygame.image.load(caminho_menu).convert()
        Fundo_Menu_Novo = pygame.transform.scale(Fundo_Menu_Novo, (WIDTH, HEIGHT))
        
        sprites = {}
        Fundo = None
        chao_tiles = {}
        plat_tiles = {}
        
        for nome, caminho in Imagens.items():
            caminho_absolute = os.path.join(BASE_DIR, caminho)
            imagem_crua = pygame.image.load(caminho_absolute if 'caminho_absolute' in locals() else caminho)
            
            if nome == "Imagem_fundo":
                sprites[nome] = pygame.transform.scale(imagem_crua, (WIDTH, HEIGHT)).convert()
                Fundo = sprites[nome]
            if nome == "engrenagem":
                sprites[nome] = pygame.transform.scale(imagem_crua, (50, 50)).convert_alpha()
                engrenagem = sprites[nome]
            elif nome == "volume":
                sprites[nome] = pygame.transform.scale(imagem_crua, (50, 50)).convert_alpha()
                volume = sprites[nome]
            elif nome == "mutado":
                sprites[nome] = pygame.transform.scale(imagem_crua, (50, 50)).convert_alpha()
                mutado = sprites[nome]
            elif nome.startswith("chao_"):
                chao_tiles[nome] = pygame.transform.scale(imagem_crua, (TILE_SIZE, TILE_SIZE)).convert_alpha()
            elif nome.startswith("plat_"):
               plat_tiles[nome] = pygame.transform.scale(imagem_crua, (TILE_SIZE, TILE_SIZE)).convert_alpha()
            
            elif nome == "entrada_templo":
                sprites[nome] = pygame.transform.scale(imagem_crua, (120, 160)).convert_alpha()
                templo = sprites[nome]
            
        botao_config = Button(
            600, 40, 50, 50,
            image=engrenagem
        )

        botao_volume, botao_controles, botao_voltar = botoes_config(font, volume)

        # --- BOTÕES DO MENU INICIAL ---
        botao_start = Button(WIDTH // 2 - 100, HEIGHT // 2 - 20, 200, 50, text="START", font=font)
        botao_quit = Button(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50, text="QUIT", font=font)

        player = Player()
        config.fase_atual = 1
        fase = Fase(config.fase_atual, chao_tiles=chao_tiles, plat_tiles=plat_tiles, entrada_templo=templo)
        camera_x = 0

        estado = "MENU" 
        motivo_derrota = "" 
        tempo_derrota = None
        tempo_transicao = None
        musica_pausada_por_efeito = False  # Controla se fomos nós que paramos a música
        perguntas_fase = []
        indice_pergunta = 0
        pergunta_atual = None
        vidas_esfinge = 3
        pontos_acumulados_quiz = 0
        mensagem_quiz = ""
        esfinge_ativada = False  # FIX: impede que a esfinge seja ativada mais de uma vez por fase


        running = True
        while running:
            keys = pygame.key.get_pressed()
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                # --- EVENTOS DO MENU INICIAL ---
                if estado == "MENU":
                    if botao_start.is_clicked(event):
                        estado = "NOME"  
                    if botao_quit.is_clicked(event):
                        running = False

                elif estado == "NOME":
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if config.nome_jogador.strip() != "":
                                estado = "JOGANDO"
                        elif event.key == pygame.K_BACKSPACE:
                            config.nome_jogador = config.nome_jogador[:-1]
                        else:
                            if event.unicode.isprintable() and len(config.nome_jogador) < 15:
                                config.nome_jogador += event.unicode

                if botao_config.is_clicked(event) and estado not in ["MENU", "NOME", "PROXIMA_FASE", "REINICIAR_FASE"]:
                    estado = "CONFIG"

                if estado == "CONFIG":
                    if botao_volume.is_clicked(event): 

                        if botao_volume.is_clicked(event):
                            if pygame.mixer.music.get_volume() > 0:
                                pygame.mixer.music.set_volume(0)
                                botao_volume.image = mutado
                            else:
                                pygame.mixer.music.set_volume(0.3)
                                botao_volume.image = volume

                    if botao_controles.is_clicked(event): estado = "CONTROLES"
                    if botao_voltar.is_clicked(event): estado = "JOGANDO"
                
                elif estado == "CONTROLES":
                    if event.type == pygame.KEYDOWN:
                        if event.key in (pygame.K_ESCAPE, pygame.K_RETURN):
                            estado = "CONFIG"

                if event.type == pygame.KEYDOWN and event.key == pygame.K_r and estado == "JOGANDO":
                    player.rect.topleft = (100, HEIGHT - 150)
                    player.vel_y = 0
                    player.pos_x = 100.0 
                    player.pos_y = float(HEIGHT - 150) 
                    estado = "JOGANDO"

                # Lógica de respostas do Quiz
                if estado == "BOSS" and event.type == pygame.KEYDOWN:
                    resposta_dada = None
                    if event.key == pygame.K_a: resposta_dada = "a"
                    if event.key == pygame.K_b: resposta_dada = "b"
                    if event.key == pygame.K_c: resposta_dada = "c"
                    if event.key == pygame.K_d: resposta_dada = "d"

                    if resposta_dada is not None:

                        acertou = (resposta_dada == pergunta_atual["resposta_correta"])

                        if indice_pergunta in (0, 1):
                            # 1ª e 2ª pergunta: usam as 3 vidas da esfinge.
                            # Errando, repete a MESMA pergunta até acertar ou as vidas acabarem.
                            if acertou:
                                mensagem_quiz = ""
                                pontos_acumulados_quiz += PONTOS_PERGUNTA[indice_pergunta]

                                if indice_pergunta == 1:
                                    # Só chega em acertar a 2ª depois de já ter acertado a 1ª,
                                    # então aqui ela acertou as duas: ganha o bônus extra
                                    pontos_acumulados_quiz += BONUS_DUPLA

                                indice_pergunta += 1
                                pergunta_atual = perguntas_fase[indice_pergunta]

                            else:
                                vidas_esfinge -= 1
                                print(f"Resposta errada! Vidas da esfinge restantes: {vidas_esfinge}")

                                if vidas_esfinge <= 0:
                                    # ACABOU AS VIDAS DA ESFINGE: volta pro começo da fase
                                    # (pontos_acumulados_quiz é descartado, nunca foi pra config.pontuacao)
                                
                                    if som_ativo:
                                        pygame.mixer.music.stop()
                                        canal_efeitos.play(erro)
                                        musica_pausada_por_efeito = True

                                        estado = "REINICIAR_FASE"
                                        motivo_derrota = "ESFINGE"
                                        tempo_derrota = pygame.time.get_ticks()

                                else:
                                    # Não perdeu tudo ainda: deixa claro que pode tentar de novo
                                    mensagem_quiz = f"Errou! Ainda restam {vidas_esfinge} vida(s), tente de novo!"
                                    # pergunta_atual continua a mesma: repete a pergunta

                        else:
                            # 3ª pergunta: é só bônus, não gasta vida, NUNCA reinicia a fase
                            if acertou:
                                pontos_acumulados_quiz += PONTOS_PERGUNTA[indice_pergunta]
                            else:
                                print("Errou a pergunta bônus, mas segue em frente!")

                            # Terminou o quiz (chegou até aqui acertando a 1ª e a 2ª): avança de fase.
                            # Só agora os pontos da tentativa são confirmados de verdade.
                            config.pontuacao += pontos_acumulados_quiz

                            if som_ativo:
                                pygame.mixer.music.stop()
                                canal_efeitos.play(acerto)
                                musica_pausada_por_efeito = True

                            if config.fase_atual < 3:

                                config.fase_atual += 1
                                config.vidas = 3

                                player.rect.topleft = (100, HEIGHT - 150)
                                player.vel_y = 0
                                player.pos_x = 100.0  
                                player.pos_y = float(HEIGHT - 150) 

                                fase = Fase(config.fase_atual, chao_tiles=chao_tiles, plat_tiles=plat_tiles, entrada_templo=templo)
                                esfinge_ativada = False  # FIX: reseta a flag para a nova fase

                                estado = "PROXIMA_FASE"
                                tempo_transicao = pygame.time.get_ticks()

                            else:

                                estado = "VENCEU"
            
            # --- ATUALIZAÇÃO DA LÓGICA DO JOGO ---
            if estado == "JOGANDO":
                player.move(keys)
                check_colisoes(player, fase)

                camera_destino = player.rect.centerx - WIDTH // 2
                camera_destino = max(0, min(camera_destino, MAP_WIDTH - WIDTH))

                camera_x += (camera_destino - camera_x) * 0.08
                if player.rect.bottom > HEIGHT:
                    config.vidas -= 1
                    player.rect.topleft = (100, HEIGHT - 150)
                    player.vel_y = 0

                    print(f"{config.nome_jogador} caiu no buraco ! Restam: {config.vidas} vidas")
                
                    if config.vidas <= 0:
                        # CAIU NO BURACO E MORREU: não toca som, reservado pra esfinge
                        estado = "REINICIAR_FASE"
                        motivo_derrota = "BURACO"
                        tempo_derrota = pygame.time.get_ticks()

                # FIX: só ativa a esfinge se ainda não foi ativada nesta fase
                if not esfinge_ativada and player.rect.colliderect(fase.esfinge_rect):
                    esfinge_ativada = True

                    perguntas_fase = random.sample(
                        PERGUNTAS_POR_FASE[config.fase_atual],
                        min(3, len(PERGUNTAS_POR_FASE[config.fase_atual]))
                    )

                    indice_pergunta = 0
                    vidas_esfinge = 3
                    pontos_acumulados_quiz = 0
                    mensagem_quiz = ""
                    pergunta_atual = perguntas_fase[0]

                    estado = "BOSS"

            # CONTEXTO DE ÁUDIO AUTOMÁTICO: Se o efeito acabou de tocar, volta a trilha sonora
            if som_ativo:
                if musica_pausada_por_efeito and not canal_efeitos.get_busy():
                    if estado not in ["VENCEU"]:  # Não reinicia a trilha se o jogo acabou
                        pygame.mixer.music.play(-1)
                    musica_pausada_por_efeito = False

            # --- DESENHO NA TELA ---
            if estado == "MENU":
                screen.blit(Fundo_Menu_Novo, (0, 0)) 
                draw_text(screen, "DESERT TRAIL - A Jornada do Explorador", WIDTH//2 - 270, HEIGHT//2 - 120, 40, BLACK)
                botao_start.draw(screen)
                botao_quit.draw(screen)

            elif estado == "NOME":
                screen.fill(SAND_YELLOW)
                draw_text(screen, "DESERT TRAIL", WIDTH// 2 - 120, HEIGHT//2 - 120, 40, RED)
                draw_text(screen, "Digite o nome do Explorador:", WIDTH//2 - 150, HEIGHT//2 - 40, 28, BLACK)
                draw_text(screen, config.nome_jogador + "|", WIDTH//2 - 100, HEIGHT//2 + 10, 36, BLUE)
                draw_text(screen, "Aperte ENTER para começar", WIDTH//2 - 130, HEIGHT//2 + 80, 24, BLACK)

            else:
                fundo_x = -(camera_x * 0.5)
                for x in range(-WIDTH, MAP_WIDTH, WIDTH):
                    screen.blit(Fundo, (x + fundo_x, 0))

                if estado not in ["PROXIMA_FASE", "REINICIAR_FASE"]:
                    botao_config.draw(screen)
                
                if estado == "JOGANDO":
                    fase.draw(screen, camera_x)
                    player.draw(screen, camera_x)
                    
                    draw_text(screen, f"Fase Atual: {config.fase_atual} / 3", 20, 20, 28, BLUE)
                    draw_text(screen, f"Explorador: {config.nome_jogador}", 20, 70, 26, BLACK)
                    
                    draw_text(screen, f"Pontuação: {config.pontuacao}", 600, 530, 26, BLACK)
                    draw_text(screen, f"Vidas: {config.vidas}", 600, 560, 26, RED)
                
                elif estado == "CONFIG":
                    screen.fill(BLACK)
                    draw_text(screen, "CONFIGURAÇÕES", 400, 100, 50, WHITE)
                    botao_volume.draw(screen)
                    botao_controles.draw(screen)
                    botao_voltar.draw(screen)

                elif estado == "CONTROLES":

                    screen.fill(config.SAND_YELLOW)

                    draw_text(screen, "CONTROLES", 260, 40, 44, config.BLACK)

                    draw_text(screen, "Setas  : Mover", 120, 120, 30, config.BLACK)
                    draw_text(screen, "ESPAÇO : Pular", 120, 170, 30, config.BLACK)

                    pygame.draw.line(screen, config.BLACK, (80, 230), (720, 230), 2)

                    draw_text(screen, "OBJETIVO", 280, 250, 38, config.RED)

                    draw_text(screen, "Chegue até a entrada do templo.", 100, 310, 28, config.BLACK)

                    draw_text(screen,"Ao final da fase você enfrentará", 100, 350, 28, config.BLACK)

                    draw_text(screen, "a Esfinge e responderá enigmas.", 100, 385, 28, config.BLACK)

                    draw_text(screen, "Você possui 3 vidas para responder", 100, 435, 24, config.BLACK)

                    draw_text(screen, "suas 3 perguntas.", 100, 465, 24, config.BLACK)

                    draw_text(screen, "ENTER ou ESC para voltar", 220, 540, 24, config.BLUE)
                    
                elif estado == "BOSS":

                    draw_text(
                        screen,
                        f"Pergunta {indice_pergunta + 1}/3",
                        20,
                        20,
                        30,
                        RED
                    )

                    if indice_pergunta == 2:
                        draw_text(
                            screen,
                            "Última pergunta! Acerte e ganhe 100 pontos de bônus!",
                            20,
                            55,
                            24,
                            GREEN
                        )
                    elif mensagem_quiz:
                        draw_text(
                            screen,
                            mensagem_quiz,
                            20,
                            55,
                            24,
                            RED
                        )

                    desenhar_boss(
                        screen,
                        pergunta_atual,
                        config.fase_atual,
                        vidas_esfinge,
                        config.pontuacao + pontos_acumulados_quiz,
                        config.nome_jogador,
                    )

                elif estado == "PROXIMA_FASE":
                    segundos_passados = (pygame.time.get_ticks() - tempo_transicao) // 1000
                    contador = 5 - segundos_passados

                    screen.fill(SAND_YELLOW)
                    draw_text(screen, f"FASE CONCLUÍDA!", WIDTH//2 - 130, HEIGHT//2 - 60, 42, GREEN)
                    draw_text(screen, f"Muito bem {config.nome_jogador}, suas vidas recarregaram!", WIDTH//2 - 240, HEIGHT//2, 26, BLACK)
                    draw_text(screen, f"Entrando na Fase {config.fase_atual} em {contador}...", WIDTH//2 - 150, HEIGHT//2 + 50, 24, BLUE)

                    if contador <= 0:
                        estado = "JOGANDO"

                elif estado == "REINICIAR_FASE":
                    segundos_passados = (pygame.time.get_ticks() - tempo_derrota) // 1000
                    contador = 5 - segundos_passados

                    screen.fill(BLACK)
                    draw_text(screen, "VOCÊ MORREU!", WIDTH//2 - 110, HEIGHT//2 - 60, 42, RED)
                    if motivo_derrota == "BURACO":
                        draw_text(screen, f"{config.nome_jogador} caiu no abismo...", WIDTH//2 - 150, HEIGHT//2, 26, WHITE)
                    else:
                        draw_text(screen, "A Esfinge te devorou por errar a pergunta!", WIDTH//2 - 220, HEIGHT//2, 26, WHITE)
                        
                    draw_text(screen, f"Reiniciando a Fase {config.fase_atual} com vidas cheias em {contador}...", WIDTH//2 - 250, HEIGHT//2 + 60, 24, RED)

                    if contador <= 0:
                        config.vidas = 3 
                        player.rect.topleft = (100, HEIGHT - 150)
                        player.vel_y = 0
                        player.pos_x = 100.0
                        player.pos_y = float(HEIGHT - 150)
                        fase = Fase(config.fase_atual, chao_tiles=chao_tiles, plat_tiles=plat_tiles, entrada_templo=templo)
                        esfinge_ativada = False  # FIX: reseta a flag ao reiniciar a fase
                        estado = "JOGANDO"

                elif estado == "VENCEU":
                    if not hasattr(config, "salvou_ranking"):
                        with open("ranking.txt", "a", encoding="utf-8") as arq:
                            arq.write(f"{config.nome_jogador} - {config.pontuacao}\n")
                        config.salvou_ranking = True

                    draw_text(screen, "PARABÉNS! JOGO CONCLUÍDO!", WIDTH//2 - 220, HEIGHT//2 - 50, 45, GREEN)
                    draw_text(screen, f"Você superou todas as 3 fases do Deserto, {config.nome_jogador}!", WIDTH//2 - 270, HEIGHT//2 + 10, 26, BLACK)
                    draw_text(screen, f"Pontuação Final: {config.pontuacao}", WIDTH//2 - 110, HEIGHT//2 + 60, 26, BLUE)

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Jogo.main()