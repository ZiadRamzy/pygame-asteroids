# screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# colors (R,G,B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)

# game title
GAME_TITLE = "ASTEROIDS CLONE"

# game states
GAME_STATE_MENU  = "MENU"
GAME_STATE_PLAYING = "PLAYING"

# ship pysics
SHIP_ROTATION_SPEED = 3  # degrees per frame
SHIP_THRUST = 0.1  # acceleration when thrusting
SHIP_FRICTION = 0.99 # facotr multiplied to velocity for each frame

# bullet settings
BULLET_SPEED = 6
BULLET_RADIUS = 3
BULLET_LIFETIME = 60

# asteroid settings
ASTEROID_START_SIZE = 1.0
ASTEROID_SPLIT_SCALE = 0.5
ASTEROID_MIN_SIZE = 0.25
ASTEROID_SPLIT_SPEED_MULTIPLIER = 1.5
