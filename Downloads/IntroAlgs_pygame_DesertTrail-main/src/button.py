import pygame
import src.config as config


class Button:
    def __init__(self, x, y, width, height,
                 text=None, image=None, font=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text      # Texto exibido no botão (caso não seja uma imagem)
        self.image = image    # Imagem exibida no botão (ex.: engrenagem)
        self.font = font      # Fonte utilizada para renderizar o texto

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()

        # Altera a cor do botão quando o mouse passa por cima (efeito hover)
        color = (
            config.DARK_YELLOW
            if self.rect.collidepoint(mouse_pos)
            else config.SAND_YELLOW
        )

        pygame.draw.rect(
            surface,
            color,
            self.rect,
            border_radius=8
        )

        # Desenha uma imagem dentro do botão
        if self.image:
            image_rect = self.image.get_rect(
                center=self.rect.center
            )
            surface.blit(self.image, image_rect)

        # Desenha um texto dentro do botão
        elif self.text:
            text_surface = self.font.render(
                self.text,
                True,
                config.WHITE
            )

            text_rect = text_surface.get_rect(
                center=self.rect.center
            )

            surface.blit(text_surface, text_rect)

    # Verifica se o botão foi clicado com o botão esquerdo do mouse
    def is_clicked(self, event):
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )


def botoes_config(font, volume_img):
    botao_volume = Button( 400, 250, 300, 60, image=volume_img, font=font)

    botao_controles = Button( 400, 350, 300, 60, text="Controles", font=font )

    botao_voltar = Button( 400, 450, 300, 60, text="Voltar", font=font)

    return (botao_volume, botao_controles, botao_voltar)