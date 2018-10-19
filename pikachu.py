import pygame


class Pikachu():

    def __init__(self, sets, screen):
        self.sets = sets
        self.screen = screen   # Where (what screen) we put pikachu
        self.image = pygame.image.load('images/pikachu.bmp')  # surface object
        self.image = pygame.transform.scale(self.image, (45, 60))  # rescale
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()  # the surface is treat as rect to simplify the shape
        # rect  attributes : location center, centerx (x-index of the center point), centery
        # another attributes x, y the left-up corner coordinate
        # locate the new pikachu
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom
        self.centerxindex = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:  # add moving range limit
            self.centerxindex += self.sets.speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerxindex -= self.sets.speed_factor
        self.rect.centerx = self.centerxindex

    def blitme(self):
        self.screen.blit(self.image, self.rect)
