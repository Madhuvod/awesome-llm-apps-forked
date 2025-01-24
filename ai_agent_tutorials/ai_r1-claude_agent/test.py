from e2b_code_interpreter import Sandbox
from typing import Literal, Dict
# Define the code to be executed
code_to_run = """
import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

center_pos = pygame.Vector2(screen.get_width() // 2, screen.get_height() // 2)
original_vertices = [
    pygame.Vector2(0, -20),  # tip
    pygame.Vector2(10, 10),
    pygame.Vector2(-10, 10)
]
current_angle = 0  # radians
lerp_speed = 5.0  # higher is faster
rotation_speed = 5.0  # radians per second

while running:
    dt = clock.tick(60) / 1000  # dt in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mouse_pos = pygame.mouse.get_pos()
    target_pos = pygame.Vector2(mouse_pos)

    # Update position
    alpha = lerp_speed * dt
    alpha = min(alpha, 1)
    center_pos = center_pos.lerp(target_pos, alpha)

    # Update rotation
    dx = target_pos.x - center_pos.x
    dy = target_pos.y - center_pos.y
    if dx == 0 and dy == 0:
        target_angle = current_angle  # avoid division by zero
    else:
        target_angle = math.atan2(dy, dx) - math.pi / 2

    angle_diff = target_angle - current_angle
    angle_diff = (angle_diff + math.pi) % (2 * math.pi) - math.pi  # wrap to [-pi, pi]

    current_angle += angle_diff * rotation_speed * dt

    # Rotate vertices
    rotated_vertices = [
        (v.rotate(math.degrees(current_angle)) + center_pos) for v in original_vertices
    ]

    # Draw
    screen.fill((0, 0, 0))
    pygame.draw.polygon(screen, (255, 0, 0), rotated_vertices)
    pygame.display.flip()

pygame.quit()
"""
dub = """import pygame
pygame.init()
pygame.display.set_mode((800, 600)).fill((255, 0, 0))
pygame.display.flip()"""
# Execute Python code inside the sandbox
sbx = Sandbox(api_key="e2b_72f487568fb34579c408f2df8ba8af993e81705e")
sbx.commands.run("pip install pygame")
execution = sbx.run_code(
    code=dub,
    language='python',
)
result = execution
print(result)

