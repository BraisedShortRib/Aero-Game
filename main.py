import pygame
import sys
import random
from plane import Plane
from projectile import Projectile


def shoot_projectile(projectiles_group, screen_width, screen_height):
    y = random.randint(0, screen_height)
    max_speed = 8
    speed = random.randint(1, max_speed)
    projectile = Projectile(screen_width, y, speed)
    projectiles_group.add(projectile)


def main():
    random.seed()
    pygame.init()
    monitor_info = pygame.display.Info()
    size = width, height = monitor_info.current_w, monitor_info.current_h

    screen = pygame.display.set_mode(size)

    start_background = pygame.image.load(
        "resources/start_background.jpg").convert()
    start_background = pygame.transform.scale(start_background,
                                              (width, height))
    background = pygame.image.load("resources/background.jpg").convert()
    background = pygame.transform.scale(background, (width, height))

    end_background = pygame.image.load(
        "resources/end_background.jpg").convert()
    end_background = pygame.transform.scale(end_background, (width, height))
    plane = Plane()
    projectiles = pygame.sprite.Group()
    shoot_projectile(projectiles, width, height)
    plane_group = pygame.sprite.Group()
    plane_group.add(plane)

    # Change behavior so key registers as pressed again if its held, every 1 ms
    pygame.key.set_repeat(1)
    PROJECTILE_EVENT = pygame.USEREVENT + 1
    time_step = 300
    pygame.time.set_timer(PROJECTILE_EVENT, time_step)


    start_screen = True
    running_game = True
    end_screen = False

    screen.blit(start_background, (0,0))
    pygame.display.flip()
    while start_screen:
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_SPACE]:
            start_screen = False

    screen.blit(background, (0, 0)) 
    pygame.display.flip()
    while running_game:
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == PROJECTILE_EVENT:
                shoot_projectile(projectiles, width, height)
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
            running_game = False
            end_screen = True
            print("switching to end screen")
        else:
            print("not colliding")
        plane_group.update()
        projectiles.update()
        screen.blit(background, (0, 0))
        plane_group.draw(screen)
        projectiles.draw(screen)
        pygame.display.flip()

    screen.blit(end_background, (0, 0))
    pygame.display.flip()
    while end_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    main()
