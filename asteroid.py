import pygame
import random
import math
from constants import (
    ASTEROID_MIN_SIZE,
    ASTEROID_SCORE_VALUES,
    ASTEROID_SPLIT_SCALE,
    ASTEROID_SPLIT_SPEED_MULTIPLIER,
    WHITE,
)
from game_objects import GameObject


class Asteroid(GameObject):
    def __init__(self, position, size_factor=1.0, speed_multiplier=1.0):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(0.5, 2) * speed_multiplier
        velocity = (speed * math.cos(angle), speed * math.sin(angle))

        radius = 30 * size_factor

        super().__init__(
            position=position,
            velocity=velocity,
            radius=radius
        )
        self.color = WHITE
        self.size_factor = size_factor
        self.speed_multiplier = speed_multiplier
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

    def split(self):
        if self.size_factor <= ASTEROID_MIN_SIZE:
            return []

        fragments = []
        for angle_offset in (-0.5, 0.5):
            speed = math.hypot(self.velocity[0], self.velocity[1]) * ASTEROID_SPLIT_SPEED_MULTIPLIER
            heading = math.atan2(self.velocity[1], self.velocity[0]) + angle_offset
            velocity = (speed * math.cos(heading), speed * math.sin(heading))

            fragment = Asteroid(
                position=self.position,
                size_factor=self.size_factor * ASTEROID_SPLIT_SCALE,
                speed_multiplier=self.speed_multiplier,
            )
            fragment.velocity = velocity
            fragments.append(fragment)

        return fragments

    def score_value(self):
        return ASTEROID_SCORE_VALUES.get(self.size_factor, 0)
