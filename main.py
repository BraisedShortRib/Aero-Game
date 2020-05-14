import pygame
import sys
from plane import Plane
from projectile import Projectile


#TODO:
# randomize missile starting position
# Create missiles on a time interval
# Maybe make the missiles explode if they hit you? Show that you fucked up
# Make sure this still compiles on windows
# Make it so it will actually exit the game if you click the x
def main():
    pygame.init()
    monitor_info = pygame.display.Info()
    size = width, height = monitor_info.current_w, monitor_info.current_h

    screen = pygame.display.set_mode(size)
    background = pygame.image.load("resources/background.jpg").convert()
    background = pygame.transform.scale(background, (width, height))
    screen.blit(background, (0, 0))
    plane = Plane()
    projectile = Projectile(width)
    projectiles = pygame.sprite.Group()
    projectiles.add(projectile)
    plane_group = pygame.sprite.Group()
    plane_group.add(plane)

    # Change behavior so key registers as pressed again if its held, every 1 ms
    pygame.key.set_repeat(1)

    while True:
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("exiting")
                sys.exit()
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_DOWN] and not plane.out_bottom_bounds(height):
            plane.fly_down()
        if keypressed[pygame.K_UP] and not plane.out_top_bounds():
            plane.fly_up()
        if keypressed[pygame.K_RIGHT] and not plane.out_right_bounds(width):
            plane.fly_right()
        if keypressed[pygame.K_LEFT] and not plane.out_left_bounds():
            plane.fly_left()
        if pygame.sprite.spritecollide(plane, projectiles, False):
            print("colliding")
        else:
            print("not colliding")
        plane_group.update()
        projectiles.update()
        screen.blit(background, (0, 0))
        plane_group.draw(screen)
        projectiles.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
