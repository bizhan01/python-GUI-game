import pygame
import pybullet as p

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Initialize PyBullet
p.connect(p.GUI)
p.setGravity(0, 0, -9.81)

# Create a ground plane
p.createCollisionShape(p.GEOM_PLANE)
p.createMultiBody(0, 0)

# Create a robot model (replace with your own robot model)
robot_model = p.createCapsule(radius=0.5, height=2)

# Set the robot's initial position and orientation
p.resetBasePositionAndOrientation(robot_model, [0, 0, 1], [0, 0, 0, 1])

# Main loop
running = True
while running:
    # Clear the screen
    screen.fill((255, 255, 255))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get robot's current position and orientation
    pos, orn = p.getBasePositionAndOrientation(robot_model)

    # Draw the robot on the screen
    robot_size = 50
    robot_pos = (width // 2, height // 2)
    pygame.draw.circle(screen, (255, 0, 0), robot_pos, robot_size)

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 FPS

# Clean up resources
p.disconnect()
pygame.quit()