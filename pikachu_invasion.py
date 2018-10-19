import sys
import pygame
from settings import Settings
from pikachu import Pikachu


def run_game():
    pygame.init()
    ai_settings = Settings()
    background = pygame.image.load(r"images/bg.png")
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('pikachu invasion')  # set screen object
    pikachu = Pikachu(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background, (0, 0))
        # screen.fill(ai_settings.bg_color)
        pikachu.blitme()
        pygame.display.flip()


run_game()
