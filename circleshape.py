import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius


# method to teste if collides
    def collide_test(self, other):
        dist = pygame.math.Vector2.distance_to(self.position, other.position)
        if dist < self.radius + other.radius:
            return True
        else:
            return False


# functions to be override by sub-classes
    def draw(self, screen):
        pass

    def update(self, dt):
        pass