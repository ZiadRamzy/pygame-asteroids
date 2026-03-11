import math
import pygame

from constants import BULLET_LIFETIME, BULLET_RADIUS, BULLET_SPEED, WHITE
from game_objects import GameObject


class Bullet(GameObject):
    def __init__(self, position, heading, ship_velocity=(0, 0)):
        angle_rad = math.radians(heading - 90)
        velocity = (
            ship_velocity[0] + BULLET_SPEED * math.cos(angle_rad),
            ship_velocity[1] + BULLET_SPEED * math.sin(angle_rad),
        )

        super().__init__(position=position, velocity=velocity, radius=BULLET_RADIUS)
        self.color = WHITE
        self.remaining_frames = BULLET_LIFETIME

    def move(self):
        super().move()
        self.remaining_frames -= 1

    def is_expired(self):
        return self.remaining_frames <= 0

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            self.color,
            (int(self.position[0]), int(self.position[1])),
            self.radius,
            1,
        )
