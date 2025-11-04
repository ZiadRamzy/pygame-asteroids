import pygame
import random
import math
from constants import WHITE
from game_objects import GameObject


class Asteroid(GameObject):
    def __init__(self, position, size_factor=1.0):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(0.5, 2)
        velocity = (speed * math.cos(angle), speed * math.sin(angle))

        radius = 30 * size_factor

        super().__init__(
            position=position,
            velocity=velocity,
            radius=radius
        )
        self.color = WHITE
        self.points = self._generate_polygon(radius)

    def _generate_polygon(self, radius):
        """
        Generates a simple irregular polygon shape for the asteroid
        """
        num_points = 5
        points = []
        for i in range(num_points):
            angle = 2 * math.pi * (i / num_points)
            r = radius * random.uniform(0.8, 1.2)
            x = r * math.cos(angle)
            y = r* math.sin(angle)
            points.append((x, y))
        
        return points
    
    def draw(self, surface):
        """
        Draws the irregular polygon centered at the objects's position
        """
        screen_points = [
            (int(self.position[0] + px), int(self.position[1] + py))
            for px, py in self.points
        ]
        pygame.draw.polygon(surface, self.color, screen_points, 1)
