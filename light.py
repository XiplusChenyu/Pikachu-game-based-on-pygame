import pygame
from pygame.sprite import Sprite


class Light(Sprite):

    def __init__(self, sets, screen, pikachu):
        super(Light, self).__init__()
        # insert lightning image
        self.image = pygame.image.load('images/light.png')
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()

        # set the initial location
        self.screen = screen
        self.rect.centerx = pikachu.rect.centerx
        self.rect.top = pikachu.rect.top

        # set the location with float
        self.location = float(self.rect.y)

        # speed
        self.speed_factor = sets.light_speed_factor

    def update(self):
        self.location -= self.speed_factor
        self.rect.y = self.location

    def blitme(self):
        self.screen.blit(self.image, self.rect)
