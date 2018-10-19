import sys
import pygame


def check_events_keydown(event, pikachu):
    if event.key == pygame.K_RIGHT:
        pikachu.moving_right = True
    elif event.key == pygame.K_LEFT:
        pikachu.moving_left = True


def check_events_keyup(event, pikachu):
    if event.key == pygame.K_RIGHT:
        pikachu.moving_right = False
    elif event.key == pygame.K_LEFT:
        pikachu.moving_left = False


def check_events(pikachu):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event, pikachu)
        elif event.type == pygame.KEYUP:
            check_events_keyup(event, pikachu)


def update_screen(bg, screen, pikachu):
    screen.blit(bg, (0, 0))
    pikachu.blitme()
    pygame.display.flip()

