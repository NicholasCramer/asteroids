import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_angle = random.uniform(20, 50)
        asteroid_1_angle = self.velocity.rotate(new_angle)
        asteroid_2_angle = self.velocity.rotate(-new_angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_rad)
        asteroid_1.velocity = asteroid_1_angle * 1.2
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_rad)
        asteroid_2.velocity = asteroid_2_angle * 1.2
        