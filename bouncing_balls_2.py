import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Ball:
    def __init__(self, x, y, vx, vy, radius, color):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.radius = radius
        self.color = color

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Bounce off walls
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.vx *= -1
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.vy *= -1

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def collide(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        distance = math.hypot(dx, dy)
        
        if distance < self.radius + other.radius:  # Collision detected
            self.vx, other.vx = other.vx, self.vx
            self.vy, other.vy = other.vy, self.vy

# Create balls
balls = [Ball(random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50),
              random.randint(-5, 5), random.randint(-5, 5), 20, (255, 0, 0)) for _ in range(5)]

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i, ball in enumerate(balls):
        ball.move()
        ball.draw()
        for j in range(i + 1, len(balls)):
            ball.collide(balls[j])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
