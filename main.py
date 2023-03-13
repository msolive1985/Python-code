import pygame
import numpy as np

# Set up the game screen
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Game")

# Set up game variables
player_position = np.array([screen_width//2, screen_height//2])
player_speed = 5
player_color = (255, 255, 0)
player_radius = 20

enemy_position = np.array([screen_width//3, screen_height//3])
enemy_speed = 3
enemy_color = (255, 0, 0)
enemy_radius = 15

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_position[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_position[0] += player_speed
    if keys[pygame.K_UP]:
        player_position[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_position[1] += player_speed

    # Move the enemy towards the player
    direction = player_position - enemy_position
    direction = direction / np.linalg.norm(direction)
    enemy_position += direction * enemy_speed

    # Check for collision between player and enemy
    distance = np.linalg.norm(player_position - enemy_position)
    if distance < player_radius + enemy_radius:
        print("Game over!")
        running = False

    # Draw the player and enemy on the screen
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, player_color, player_position, player_radius)
    pygame.draw.circle(screen, enemy_color, enemy_position, enemy_radius)
    pygame.display.update()

    # Set the game's frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
