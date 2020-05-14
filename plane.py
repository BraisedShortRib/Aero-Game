import pygame


class Plane(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0)):
        super(Plane, self).__init__()
        self.image = pygame.image.load("resources/airplane.png")
        self.rect = self.image.get_rect()
        self.vertical_speed = 3
        self.horizontal_speed = 5

    def update(self):
        # all updating done through directly modifying rect object through other method
        pass

    def fly_up(self):
        self.rect.y -= self.vertical_speed

    def fly_down(self):
        self.rect.y += self.vertical_speed

    def fly_right(self):
        self.rect.x += self.horizontal_speed

    def fly_left(self):
        self.rect.x -= self.horizontal_speed

    def out_top_bounds(self):
        return self.rect.top < 0

    def out_bottom_bounds(self, height):
        return self.rect.bottom > height

    def out_right_bounds(self, width):
        return self.rect.right > width

    def out_left_bounds(self):
        return self.rect.left < 0
