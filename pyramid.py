import pygame

# Initialize Pygame
pygame.init()

# Window dimensions
WINDOW_WIDTH = 1027
WINDOW_HEIGHT = 768
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Cube dimensions
CUBE_WIDTH = 100
CUBE_HEIGHT = 50
DEPTH = 50

# Define colors
YELLOW = (253, 249, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

def draw_isometric_cube(screen, center, color):
    """Draws an isometric cube given the center coordinate."""
    x, y = center

    # Top face (yellow)
    pygame.draw.polygon(screen, YELLOW, [
        (x, y),
        (x - CUBE_WIDTH // 2, y - CUBE_HEIGHT // 2),
        (x, y - CUBE_HEIGHT),
        (x + CUBE_WIDTH // 2, y - CUBE_HEIGHT // 2)
    ])

    # Left face (red)
    pygame.draw.polygon(screen, RED, [
        (x, y),
        (x - CUBE_WIDTH // 2, y - CUBE_HEIGHT // 2),
        (x - CUBE_WIDTH // 2, y - CUBE_HEIGHT // 2 + DEPTH),
        (x, y + DEPTH)
    ])

    # Right face (blue)
    pygame.draw.polygon(screen, BLUE, [
        (x, y),
        (x + CUBE_WIDTH // 2, y - CUBE_HEIGHT // 2),
        (x + CUBE_WIDTH // 2, y - CUBE_HEIGHT // 2 + DEPTH),
        (x, y + DEPTH)
    ])

def draw_pyramid(screen, base_length):
    """Draws a pyramid of cubes with the given base length."""
    # The starting point is adjusted to center the pyramid
    start_x = WINDOW_WIDTH // 2 + (CUBE_WIDTH // 2 * base_length // 2) - CUBE_WIDTH // 2
    start_y = WINDOW_HEIGHT // 2 - (DEPTH * base_length // 2)

    for row in range(base_length):
        for col in range(row + 1):
            x = start_x + (CUBE_WIDTH * col) - (CUBE_WIDTH // 2 * row)
            y = start_y + (CUBE_HEIGHT * 1.6 * row)
            draw_isometric_cube(screen, (x, y), YELLOW)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_pyramid(screen, 7)  # Draw a pyramid with 7 base cubes
    pygame.display.flip()

pygame.quit()
