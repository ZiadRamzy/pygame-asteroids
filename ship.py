import pygame
import math
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE
from game_objects import GameObject

class Ship(GameObject):
    def __init__(self):
        super().__init__(
            position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
            velocity=(0, 0),
            radius=20
        )
        self.color = WHITE
        self.heading = 0  # angle in degress for example 0 is up
    
    def draw (self, surface):
        """
        Draws the trianglular ship shape
        """
        size = 15

        points_0 = [
            (size, 0),  # nose
            (-size * 0.7, -size * 0.5),  # back-left
            (-size * 0.7, size * 0.5)  # back-right
        ]

        rotated_points = []
        angle_rad = math.radians(self.heading - 90)

        for px, py in points_0:
            qx = px * math.cos(angle_rad) - py * math.sin(angle_rad)
            qy = px * math.sin(angle_rad) + py * math.cos(angle_rad)

            rotated_points.append(
                (int(self.position[0] + qx), int(self.position[1] + qy))
            )
        
        pygame.draw.polygon(surface, self.color, rotated_points, 2)