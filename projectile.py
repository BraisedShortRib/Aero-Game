import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, width):
        super(Projectile, self).__init__()
        self.image = pygame.image.load("resources/projectile.png")
        self.rect = self.image.get_rect()
        # positions below will be randomized eventually
        self.rect.x = width
        self.rect.y = 50
        self.speed = 3
    def update(self):
        self.rect.x -=3
