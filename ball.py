import pygame
from pygame.sprite import Sprite


class Ball(Sprite):

    def __init__(self, sets, screen):
        super(Ball, self).__init__()
        self.screen = screen
        self.sets = sets
        self.image = pygame.image.load('images/balls.png')
        self.image = pygame.transform.scale(self.image, (28, 28))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= screen_rect.left:
            return True

    def update(self):
        self.x += self.sets.ball_speed_factor*self.sets.balls_direction  # how they move in x direction
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
