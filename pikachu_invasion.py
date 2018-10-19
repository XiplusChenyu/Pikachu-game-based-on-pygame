import sys
import pygame
from settings import Settings
from pikachu import Pikachu
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    background = pygame.image.load(r"images/bg.png")
    background = pygame.transform.scale(background, (480, 300))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('pikachu invasion')  # set screen object
    pikachu = Pikachu(screen)
    while True:
        gf.check_events(pikachu)
        pikachu.update()
        gf.update_screen(background, screen, pikachu)


run_game()
