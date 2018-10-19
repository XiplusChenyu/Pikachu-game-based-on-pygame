import sys
import pygame


def check_events(pikachu):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pikachu.moving_right = True
                # pikachu.rect.centerx += 3
            elif event.key == pygame.K_LEFT:
                # pikachu.rect.centerx -= 3
                pikachu.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                pikachu.moving_right = False
                # pikachu.rect.centerx += 3
            elif event.key == pygame.K_LEFT:
                # pikachu.rect.centerx -= 3
                pikachu.moving_left = False




def update_screen(bg, screen, pikachu):
    screen.blit(bg, (0, 0))
    # screen.fill(ai_settings.bg_color)
    pikachu.blitme()
    pygame.display.flip()

