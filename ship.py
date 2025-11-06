import pygame
import math
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, SHIP_ROTATION_SPEED, SHIP_FRICTION, SHIP_THRUST
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

        self.is_thrusting = False
        self.rotation_direction = 0  # -1 left, 1 right, 0 none

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
    
    def rotate(self):
        """
        Change the ship's heading based on the rotation_direction
        """
        self.heading += self.rotation_direction * SHIP_ROTATION_SPEED
        self.heading %= 360

    def thrust(self):
        """
        Applies acceleration in the direction the ship is facing
        """
        if self.is_thrusting:
            angle_rad = math.radians(self.heading - 90)

            thrust_x = SHIP_THRUST * math.cos(angle_rad)
            thrust_y = SHIP_THRUST * math.sin(angle_rad)

            current_vx, current_vy = self.velocity
            new_vx = current_vx + thrust_x
            new_vy = current_vy + thrust_y

            self.velocity = (new_vx, new_vy)

    def apply_friction(self):
        """
        Slows the ship's velocity over time (drag)
        """
        current_vx, current_vy = self.velocity
        new_vx = current_vx * SHIP_FRICTION
        new_vy = current_vy * SHIP_FRICTION
        self.velocity = (new_vx, new_vy)

    def move(self):
        """
        Overrides thebase move to include thrust, rotation, and friction
        """
        self.rotate()
        self.thrust()
        self.apply_friction()

        super().move()