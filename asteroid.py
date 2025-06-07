import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("White"), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        random_angle = random.uniform(20, 50)
        u_velocity = self.velocity.rotate(random_angle) * 1.2
        d_velocity = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        

        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_a.velocity = u_velocity
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b.velocity = d_velocity
        
        