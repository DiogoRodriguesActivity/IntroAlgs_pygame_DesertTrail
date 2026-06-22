import pygame
from src.config import WIDTH, HEIGHT, RED, TILE_SIZE


class Plataforma(object):
    def __init__(self, x, y, width, height, tiles, tipo="plataforma"):
        self.rect = pygame.Rect(x, y, width, height)
        self.tiles = tiles
        self.tipo = tipo  # "chao" ou "plataforma"

    def draw(self, screen, camera_x):
        draw_x = self.rect.x - camera_x
        colunas = max(1, self.rect.width // TILE_SIZE)
        linhas = max(1, self.rect.height // TILE_SIZE)

        if self.tipo == "chao":
            for row in range(linhas):
                for col in range(colunas):
                    tx = draw_x + col * TILE_SIZE
                    ty = self.rect.y + row * TILE_SIZE

                    if col == 0:
                        chave = "chao_topo_esq" if row == 0 else "chao_fill_esq"
                    elif col == colunas - 1:
                        chave = "chao_topo_dir" if row == 0 else "chao_fill_dir"
                    else:
                        chave = "chao_topo_mid" if row == 0 else "chao_fill_mid"

                    screen.blit(self.tiles[chave], (tx, ty))

        elif self.tipo == "plataforma":
            for col in range(colunas):
                tx = draw_x + col * TILE_SIZE
                if col == 0:
                    chave = "plat_esq"
                elif col == colunas - 1:
                    chave = "plat_dir"
                else:
                    chave = "plat_mid"
                screen.blit(self.tiles[chave], (tx, self.rect.y))


class Fase(object):
    def __init__(self, nivel=1, chao_tiles=None, plat_tiles=None, entrada_templo=None):
        self.plataformas = []
        self.nivel = nivel
        self.tiles = {**(chao_tiles or {}), **(plat_tiles or {})}
        self.entrada_templo = entrada_templo
        self.gerar_fase()

    def gerar_fase(self):
        self.plataformas = []
        t = self.tiles

        self.plataformas.append(Plataforma(0, HEIGHT - 64, 400, 128, t, "chao"))

        if self.nivel == 1:
            self.plataformas.append(Plataforma(500,  HEIGHT - 150, 320, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(900,  HEIGHT - 250, 384, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(1400, HEIGHT - 120, 320, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(1800, HEIGHT - 220, 384, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(2300, HEIGHT - 150, 320, 64, t, "plataforma"))
            
            self.esfinge_rect = pygame.Rect(2800, HEIGHT - 150, 60, 100)

        elif self.nivel == 2:
            self.plataformas.append(Plataforma(500,  HEIGHT - 120, 192, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(850,  HEIGHT - 220, 192, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(1200, HEIGHT - 320, 192, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(1550, HEIGHT - 200, 192, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(1900, HEIGHT - 120, 192, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(2250, HEIGHT - 220, 192, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(2520, HEIGHT - 150, 128, 64, t, "plataforma"))
            
            self.esfinge_rect = pygame.Rect(2750, HEIGHT - 250, 60, 100)

        elif self.nivel == 3:
            self.plataformas.append(Plataforma(550,  HEIGHT - 150, 128, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(800,  HEIGHT - 280, 128, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(1100, HEIGHT - 180, 128, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(1350, HEIGHT - 280, 128, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(1600, HEIGHT - 180, 128, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(1850, HEIGHT - 280, 128, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(2100, HEIGHT - 180, 128, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(2350, HEIGHT - 280, 128, 64, t, "plataforma"))
            self.plataformas.append(Plataforma(2600, HEIGHT - 180, 192, 64, t, "plataforma"))
            
            self.esfinge_rect = pygame.Rect(2800, HEIGHT - 280, 60, 100)

    def draw(self, screen, camera_x):
        for plat in self.plataformas:
            plat.draw(screen, camera_x)
        if self.entrada_templo:

            screen.blit(
                self.entrada_templo,
                (
                    self.esfinge_rect.x - camera_x,
                    self.esfinge_rect.y
                )
            )





