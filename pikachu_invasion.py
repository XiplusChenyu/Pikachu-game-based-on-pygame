import sys
import pygame
from settings import Settings
from pikachu import Pikachu
from pygame.sprite import Group
import game_functions as gf


def run_game():
    pygame.init()
    sets = Settings()
    background = pygame.image.load(r"images/bg.png")
    background = pygame.transform.scale(background, (340, 600))
    screen = pygame.display.set_mode((sets.screen_width, sets.screen_height))
    pygame.display.set_caption('pikachu!!!')  # set screen object
    pikachu = Pikachu(sets, screen)
    lights = Group()
    balls = Group()
    gf.create_balls(sets, screen, pikachu, balls)
    while True:
        gf.check_events(sets, screen, pikachu, lights)
        pikachu.update()
        gf.update_lights(sets, screen, pikachu, balls, lights )
        gf.update_balls(sets, balls)
        gf.update_screen(background, sets, screen, pikachu, balls, lights)


run_game()
