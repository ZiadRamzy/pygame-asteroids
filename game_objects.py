import math
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def wrap_position(position, radius=0):
    """
    Calculates the wrapped position for an entity moving off-screen. 
    """

    x, y = position
    if x < -radius:
        x = SCREEN_WIDTH + radius
    elif x > SCREEN_WIDTH + radius:
        x = -radius
    if y < -radius:
        y = SCREEN_HEIGHT + radius
    elif y > SCREEN_HEIGHT + radius:
        y = -radius
    
    return (x, y)


class GameObject:
    """
    Base class for all moving game objects (ship, asteroids)
    """

    def __init__(self, position, velocity, radius):
        self.position = position
        self.velocity = velocity
        self.radius = radius

    def move(self):
        """
        Updates the position based on velocity and applies screen wrap
        """
        new_x = self.position[0] + self.velocity[0]
        new_y = self.position[1] * self.velocity[1]
        self.position = wrap_position((new_x, new_y), self.radius)
    
    def draw(self, surface):
        pass
