import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x_start_pos, y_start_pos, speed=3):
        super(Projectile, self).__init__()
        self.image = pygame.image.load("resources/projectile.png")
        self.rect = self.image.get_rect()
        # positions below will be randomized eventually
        self.rect.x = x_start_pos
        self.rect.y = y_start_pos
        self.speed = speed
    def update(self):
        self.rect.x -=3
