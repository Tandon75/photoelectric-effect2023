import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulation of Light and Balls on Metal Plate")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)
LIGHT_COLOR = (255, 255, 0)
BALL_COLOR = (255, 0, 0)

# Parameters
PLATE_WIDTH = 600
PLATE_HEIGHT = 20
LIGHT_ANGLE = 45  # in degrees
LIGHT_LENGTH = PLATE_WIDTH / math.cos(math.radians(LIGHT_ANGLE))
BALL_RADIUS = 10
BALL_SPEED = 2
BALLS_OFFSET = 30

# Plate properties
plate_x = (WIDTH - PLATE_WIDTH) // 2
plate_y = HEIGHT // 2

# Light properties
light_start_x = plate_x
light_start_y = plate_y - PLATE_HEIGHT // 2
light_end_x = light_start_x + LIGHT_LENGTH * math.cos(math.radians(LIGHT_ANGLE))
light_end_y = light_start_y - LIGHT_LENGTH * math.sin(math.radians(LIGHT_ANGLE))

# Balls properties
balls = []
ball_timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(ball_timer_event, 2000)  # 2 seconds timer

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == ball_timer_event:
            new_ball_x = plate_x + PLATE_WIDTH / 2
            new_ball_y = plate_y
            new_ball_speed = BALL_SPEED
            balls.append((new_ball_x, new_ball_y, new_ball_speed))

    # Update ball positions
    for i, ball in enumerate(balls):
        ball_x, ball_y, ball_speed = ball
        ball_y -= ball_speed
        balls[i] = (ball_x, ball_y, ball_speed)

    # Draw everything
    screen.fill(WHITE)

    # Draw the plate
    pygame.draw.rect(screen, SILVER, (plate_x, plate_y, PLATE_WIDTH, PLATE_HEIGHT))

    # Draw the incident light ray
    pygame.draw.line(screen, LIGHT_COLOR, (light_start_x, light_start_y), (light_end_x, light_end_y), 2)

    # Draw the outgoing light rays from the plate
    for i in range(5):
        outgoing_light_start_x = plate_x + i * PLATE_WIDTH / 4
        outgoing_light_start_y = plate_y
        outgoing_light_end_x = outgoing_light_start_x + LIGHT_LENGTH * math.cos(math.radians(LIGHT_ANGLE))
        outgoing_light_end_y = outgoing_light_start_y - LIGHT_LENGTH * math.sin(math.radians(LIGHT_ANGLE))
        pygame.draw.line(screen, LIGHT_COLOR, (outgoing_light_start_x, outgoing_light_start_y), (outgoing_light_end_x, outgoing_light_end_y), 2)

    # Draw the balls
    for ball in balls:
        ball_x, ball_y, _ = ball
        pygame.draw.circle(screen, BALL_COLOR, (int(ball_x), int(ball_y)), BALL_RADIUS)

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()
