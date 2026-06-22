import pygame

def check_colisoes(player, fase):
    player.on_ground = False
    
    # Colisão com o chão e plataformas
    for plat in fase.plataformas:
        if player.rect.colliderect(plat.rect):
            # Se está caindo e bate em algo
            if player.vel_y > 0 and player.rect.bottom <= plat.rect.bottom + 20:
                player.rect.bottom = plat.rect.top
                player.pos_y = player.rect.y
                player.vel_y = 0
                player.on_ground = True

def draw_text(screen, text, x, y, size=24, color=(0,0,0)):
    font = pygame.font.SysFont(None, size)
    img = font.render(text, True, color)
    screen.blit(img, (x, y))