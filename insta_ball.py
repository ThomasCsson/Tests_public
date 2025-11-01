import pygame
import pymunk
import random
import math

# Setup
WIDTH, HEIGHT = 800, 800
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 300
FPS = 60
HOLE_ANGLE_WIDTH = math.radians(240)  # ~40 degree wide hole

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0, 900)

balls = []

def angle_between(p1, p2):
    dx = p2[0] - p1[0]
    dy = p1[1] - p2[1]  # y is flipped in pygame
    return math.atan2(dy, dx) % (2 * math.pi)

def add_ball(pos=None):
    if pos is None:
        angle = random.uniform(0, 2 * math.pi)
        r = random.uniform(0, RADIUS - 30)
        x = CENTER[0] + r * math.cos(angle)
        y = CENTER[1] + r * math.sin(angle)
    else:
        x, y = pos

    mass, radius = 1, 10
    body = pymunk.Body(mass, pymunk.moment_for_circle(mass, 0, radius))
    body.position = x, y
    body.velocity = (random.uniform(-100, 100), random.uniform(-100, 100))
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 1
    shape.friction = 0.5
    space.add(body, shape)
    balls.append(shape)

# Initial ball
add_ball()

# Main loop
running = True
while running:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw circular arena with a hole at the top
    pygame.draw.circle(screen, (80, 80, 200), CENTER, RADIUS, 2)
    # Draw "hole" segment
    hole_angle_center = -math.pi / 2  # Upward
    hole_start = hole_angle_center - HOLE_ANGLE_WIDTH / 2
    hole_end = hole_angle_center + HOLE_ANGLE_WIDTH / 2

    for ball in balls[:]:
        x, y = ball.body.position
        pygame.draw.circle(screen, (255, 200, 0), (int(x), int(y)), int(ball.radius))

        dx = x - CENTER[0]
        dy = y - CENTER[1]
        dist = math.hypot(dx, dy)
        angle = angle_between(CENTER, (x, y))

        # Check for wall bounce (unless inside the hole)
        if dist > RADIUS - ball.radius:
            if not (hole_start < angle < hole_end):
                # Push back in (basic bounce)
                nx = dx / dist
                ny = dy / dist
                dot = ball.body.velocity.dot((nx, ny))
                if dot > 0:
                    bounce = pymunk.Vec2d(nx, ny) * dot * 2
                    ball.body.velocity -= bounce
            else:
                # ESCAPED through the top hole
                space.remove(ball, ball.body)
                balls.remove(ball)
                add_ball()
                add_ball()

    space.step(1 / FPS)
    pygame.display.flip()
    clock.tick(FPS)
    if len(balls)>100:
        break

pygame.quit()
