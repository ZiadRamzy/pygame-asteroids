import math


def circles_collide(first, second):
    dx = first.position[0] - second.position[0]
    dy = first.position[1] - second.position[1]
    distance = math.hypot(dx, dy)
    return distance <= first.radius + second.radius
