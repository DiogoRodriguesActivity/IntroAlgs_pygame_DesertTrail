import math
from pathlib import Path

import pygame
from src.config import *

class Player:
    _sprite = None

    def __init__(self):
        self.rect = pygame.Rect(50, HEIGHT - 150, 40, 60) # Posição inicial e tamanho
        
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)
        self.vel_y = 0
        self.vel_x = 0
        self.speed = 5
        self.jump_power = -12
        self.on_ground = False
        self.facing = 1
        self.walk_phase = 0.0
        self.animation_time = 0.0
        self.was_on_ground = False
        self.landing_frames = 0

        if Player._sprite is None:
            caminho = Path(__file__).resolve().parents[1] / "assets" / "imagens" / "heroi_pixel.png"
            imagem = pygame.image.load(str(caminho))
            recorte = imagem.get_bounding_rect(min_alpha=10)
            Player._sprite = pygame.transform.scale(imagem.subsurface(recorte), (54, 78))

    def move(self, keys):
        self.vel_x = 0
        self.animation_time += 0.08
        
        # Movimentação lateral
        if keys[pygame.K_LEFT]:
            self.vel_x = -self.speed
            self.facing = -1
        if keys[pygame.K_RIGHT]:
            self.vel_x = self.speed
            self.facing = 1

        if self.vel_x:
            self.walk_phase += 0.22
            
        # Pulo
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

       # Movimento horizontal
        self.pos_x += self.vel_x
        self.rect.x = round(self.pos_x)

        # Gravidade
        self.vel_y += GRAVITY
        self.pos_y += self.vel_y
        self.rect.y = round(self.pos_y)

        # Limitando o jogador dentro dos limites do mapa (Diogo - 14/06/2026)
        if self.rect.left < 0:
            self.rect.left = 0
            
        if self.rect.right > MAP_WIDTH:
            self.rect.right = MAP_WIDTH

     # Para saber onde desenhar na tela, você subtrai a posição da câmera (offset_x) da posição do jogador 
    def draw(self, screen, offset_x=0):
        """Desenha o arqueologo mantendo a caixa de colisao original."""
        x = int(self.rect.x - offset_x)
        y = int(self.rect.y)
        sprite = Player._sprite if self.facing == 1 else pygame.transform.flip(Player._sprite, True, False)

        # Detecta a aterrissagem para produzir um pequeno impacto visual.
        if self.on_ground and not self.was_on_ground:
            self.landing_frames = 5
        self.was_on_ground = self.on_ground

        largura, altura = 54, 78
        angulo = 0
        deslocamento_y = 0

        if not self.on_ground:
            # Na subida o heroi se estica e inclina para frente; na queda se recolhe.
            if self.vel_y < 0:
                largura, altura = 51, 83
                angulo = -7 * self.facing
            else:
                largura, altura = 57, 74
                angulo = 5 * self.facing
        elif self.landing_frames > 0:
            largura, altura = 59, 72
            self.landing_frames -= 1
        elif self.vel_x:
            # Dois passos por ciclo: sobe/desce e alterna levemente a inclinacao.
            passo = math.sin(self.walk_phase)
            deslocamento_y = int(abs(passo) * 3)
            angulo = passo * 3
            largura = 54 + int(math.cos(self.walk_phase * 2) * 2)
            altura = 78 - int(math.cos(self.walk_phase * 2) * 2)
        else:
            # Respiracao quase imperceptivel quando parado.
            deslocamento_y = int((math.sin(self.animation_time) + 1) * 0.5)

        sprite = pygame.transform.scale(sprite, (largura, altura))
        if angulo:
            sprite = pygame.transform.rotate(sprite, angulo)

        if self.on_ground:
            sombra_largura = 37 if not self.vel_x else 39
            pygame.draw.ellipse(screen, (74, 48, 34),
                                (x + 20 - sombra_largura // 2, y + 54,
                                 sombra_largura, 8))

        # Ancora a animacao nos pes para a colisao nunca parecer deslizar.
        destino = sprite.get_rect(midbottom=(x + self.rect.w // 2,
                                             y + self.rect.h - deslocamento_y))
        screen.blit(sprite, destino)
