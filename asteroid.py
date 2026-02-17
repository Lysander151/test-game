from constants import *
from circleshape import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def update(self, dt):
        self.position += (self.velocity * dt) 

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        self.kill()
        log_event("asteroid_split")
        change_vector = random.uniform(20, 50)
        first_vector = self.velocity.rotate(change_vector)
        second_vector = self.velocity.rotate(-1 * change_vector)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_new_asteroid.velocity = first_vector * 1.2
        second_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_new_asteroid.velocity = second_vector * 1.2



