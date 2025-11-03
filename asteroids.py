import pygame


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

GAME_TITLE = "ASTEROIDS CLONE"

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption(GAME_TITLE)  # window title

clock = pygame.time.Clock()  # frame rate control

font_large = pygame.font.Font(None, 74)
font_medium = pygame.font.Font(None, 50)


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


running = True
game_state = "MENU"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_state == "MENU":
        draw_start_screen()

    pygame.display.flip()  # flip contents of the display to the screen

    clock.tick(60)  # 60 frames per second

pygame.quit()
