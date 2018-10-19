import pygame


class Pikachu:
    def __init__(self, screen):
        self.screen = screen   # Where (what screen) we put pikachu
        self.image = pygame.image.load('images/pikachu.bmp')  # surface object
        self.image = pygame.transform.scale(self.image, (90, 120))  # rescale
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()  # the surface is treat as rect to simplify the shape
        # rect  attributes : location center, centerx (x-index of the center point), centery
        # another attributes x, y the left-up corner coordinate
        # locate the new pikachu
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
