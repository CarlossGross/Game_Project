import pygame
from circleshape import *
from constants import *

# initiating player class
class Player(CircleShape):
    def __init__(self, x, y,):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0


# function that makes a player looks like a triangle (size deppending on the radius)
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


# function that draws player with in white color and lines with 2 width
    def draw (self, screen):
        
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle() , width = 2)