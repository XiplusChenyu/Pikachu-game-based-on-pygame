import sys
import pygame
from light import Light


def fire_lights(sets, screen, pikachu, lights):
    if len(lights) < sets.light_limit:
        new_light = Light(sets, screen, pikachu)
        lights.add(new_light)


def check_events_keydown(event, sets, screen, pikachu, lights):
    if event.key == pygame.K_RIGHT:
        pikachu.moving_right = True
    elif event.key == pygame.K_LEFT:
        pikachu.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_lights(sets, screen, pikachu, lights)


def check_events_keyup(event, pikachu):
    if event.key == pygame.K_RIGHT:
        pikachu.moving_right = False
    elif event.key == pygame.K_LEFT:
        pikachu.moving_left = False


def check_events(sets, screen, pikachu, lights):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event, sets, screen, pikachu, lights)
        elif event.type == pygame.KEYUP:
            check_events_keyup(event, pikachu)


def update_screen(bg, sets, screen, pikachu, lights):
    screen.blit(bg, (0, 0))
    for light in lights.sprites():
        light.blitme()
    pikachu.blitme()
    pygame.display.flip()


def update_lights(lights):
    lights.update()
    for light in lights.copy():
        if light.rect.bottom <= 0:
            lights.remove(light)


