import pygame
import random
from constants import (
    SCREEN_SIZE,  SCREEN_WIDTH, BLACK, WHITE, GRAY,
    GAME_TITLE, GAME_STATE_MENU, GAME_STATE_PLAYING, SCREEN_HEIGHT
)
from ship import Ship
from asteroid import Asteroid

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(GAME_TITLE)  # window title
clock = pygame.time.Clock()  # frame rate control

font_large = pygame.font.Font(None, 74)
font_medium = pygame.font.Font(None, 50)

ship = None
asteroids = []
running = True
game_state = GAME_STATE_MENU
start_button_rect = None


def draw_text(surface, text, font, color, center_x, center_y):
    """A helper function to render and draw text to the screen"""
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (center_x, center_y)
    surface.blit(text_surface, text_rect)
    return text_rect  # rect returned for later use like button clicking


def draw_start_screen():
    """Draws the title and the Start New Game button"""
    screen.fill(BLACK)

    title_y = SCREEN_HEIGHT // 4
    draw_text(screen, GAME_TITLE, font_large, WHITE, SCREEN_WIDTH // 2, title_y)

    button_y = SCREEN_HEIGHT // 2
    start_button_rect = draw_text(
        screen, "START NEW GAME", font_medium, GRAY, SCREEN_WIDTH // 2, button_y
    )

    return start_button_rect


def start_new_game():
    """
    Initializes the entities for a new game
    """
    global ship, asteroids

    ship = Ship()
    asteroids = []

    for _ in range(4):
        position = (
            random.choice([
                random.uniform(0, SCREEN_WIDTH * 0.2),  # left edge
                random.uniform(SCREEN_WIDTH * 0.8, SCREEN_WIDTH)  # right edge
            ]),
            random.uniform(0, SCREEN_HEIGHT)
        )
        asteroids.append(Asteroid(position))


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == GAME_STATE_MENU and start_button_rect and start_button_rect.collidepoint(event.pos):
                start_new_game()
                game_state = GAME_STATE_PLAYING
        
        if game_state == GAME_STATE_PLAYING and ship:
            if event.type == pygame.KEYDOWN:
                # rotation
                if event.key == pygame.K_LEFT:
                    ship.rotation_direction = 1  # clockwise (left)
                elif event.key == pygame.K_RIGHT:
                    ship.rotation_direction = -1  # counter-clockwise (right)
                # thrust
                elif event.key == pygame.K_UP:
                    ship.is_thrusting = True
            
            elif event.type == pygame.KEYUP:
                # stop rotation
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    ship.rotation_direction = 0
                # disable accelration 
                elif event.key == pygame.K_UP:
                    ship.is_thrusting = False
    

    if game_state == GAME_STATE_PLAYING:
        ship.move()
        for asteroid in asteroids:
            asteroid.move()
    
    screen.fill(BLACK)

    if game_state == GAME_STATE_MENU:
        start_button_rect = draw_start_screen()
    elif game_state == GAME_STATE_PLAYING:
        ship.draw(screen)
        for asteroid in asteroids:
            asteroid.draw(screen)

    pygame.display.flip()  # flip contents of the display to the screen

    clock.tick(60)  # 60 frames per second

pygame.quit()
