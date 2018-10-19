import sys
import pygame
import random
from light import Light
from ball import Ball


def fire_lights(sets, screen, pikachu, lights):
    if len(lights) < sets.light_limit:
        new_light = Light(sets, screen, pikachu)
        lights.add(new_light)


def check_events_keydown(event, sets, screen, pikachu, lights):
    if event.key == pygame.K_RIGHT:
        pikachu.moving_right = True
    elif event.key == pygame.K_LEFT:
        pikachu.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_lights(sets, screen, pikachu, lights)


def check_events_keyup(event, pikachu):
    if event.key == pygame.K_RIGHT:
        pikachu.moving_right = False
    elif event.key == pygame.K_LEFT:
        pikachu.moving_left = False


def check_events(sets, screen, pikachu, lights):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event, sets, screen, pikachu, lights)
        elif event.type == pygame.KEYUP:
            check_events_keyup(event, pikachu)


def update_screen(bg, sets, screen, pikachu, balls, lights):
    screen.blit(bg, (0, 0))
    for light in lights.sprites():
        light.blitme()
    pikachu.blitme()
    balls.draw(screen)
    pygame.display.flip()


def update_lights(sets, screen, pikachu, balls, lights):
    lights.update()
    for light in lights.copy():
        if light.rect.bottom <= 0:
            lights.remove(light)
    check_kill(sets, screen, pikachu, balls, lights)


def check_kill(sets, screen, pikachu, balls, lights):
    collisions = pygame.sprite.groupcollide(lights, balls, True, True)
    # Boolean args says if the system delete crush object for both side
    if len(balls) == 0:
        lights.empty()
        create_balls(sets, screen, pikachu, balls)
        sets.light_limit += 1  # Bonus
        sets.ball_speed_factor += 2
        sets.balls_drop_speed += 2


def ballsinx(sets, ball_width):
    #  Density function
    available_x = sets.screen_width - 2 * ball_width
    ballnumx = int(available_x / (3 * ball_width))
    return ballnumx


def ballsiny(sets, pikachu_height, ball_height):
    #  Density function
    available_y = (sets.screen_height - (3 * ball_height) - 5 * pikachu_height)
    ballnumy = int(available_y/(3 * ball_height))
    return ballnumy


def create_ball(sets, screen, balls, ball_ix, ball_iy):
    ball = Ball(sets, screen)
    ball_width = ball.rect.width
    ball.x = ball_width + random.uniform(3, 4) * ball_width * ball_ix
    ball.rect.x = ball.x
    ball.rect.y = ball.rect.height + random.uniform(2, 3) * ball.rect.height * ball_iy
    balls.add(ball)


def create_balls(sets, screen, pikachu, balls):
    ball = Ball(sets, screen)
    ballnumx = ballsinx(sets, ball.rect.width)
    ballnumy = ballsiny(sets, pikachu.rect.height, ball.rect.height)
    for ball_iy in range(ballnumy):
        for ball_ix in range(ballnumx):
            create_ball(sets, screen, balls, ball_ix, ball_iy)


def check_balls_edges(sets, balls):
    for ball in balls.sprites():
        if ball.check_edge():
            change_ball_direction(sets, balls)
            break


def change_ball_direction(sets, balls):
    for ball in balls.sprites():
        ball.rect.y += sets.balls_drop_speed
    sets.balls_direction *= -1


def update_balls(sets, balls):
    check_balls_edges(sets, balls)
    balls.update()

