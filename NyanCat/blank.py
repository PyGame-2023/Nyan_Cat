import pygame
import random


# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 1400
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Game")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the player
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height // 2 - player_height // 2
player_speed = 5

# Set up the first obstacle
obstacle_width = 50
obstacle_height = random.randint(100, 400)
obstacle_x = screen_width
obstacle_y = random.randint(0, screen_height - obstacle_height)
obstacle_speed = 3

# Set up the second obstacle
obstacle2_width = 50
obstacle2_height = random.randint(100, 400)
obstacle2_x = screen_width
obstacle2_y = screen_height
obstacle2_speed = 3
obstacle2_direction = random.choice([-1, 1])  # Randomly choose a diagonal direction

# Set up the respawn timer
obstacle_respawn_time = 8000  # milliseconds
obstacle_timer = pygame.time.get_ticks()

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < screen_height - player_height:
        player_y += player_speed
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Move the first obstacle horizontally
    obstacle_x -= obstacle_speed

    # Move the second obstacle diagonally
    obstacle2_x -= obstacle2_speed
    obstacle2_y += obstacle2_speed * obstacle2_direction

    # Check for collision with the first obstacle
    if player_x + player_width > obstacle_x and player_x < obstacle_x + obstacle_width:
        if player_y < obstacle_y + obstacle_height and player_y + player_height > obstacle_y:
            running = False

    # Check for collision with the second obstacle
    if player_x + player_width > obstacle2_x and player_x < obstacle2_x + obstacle2_width:
        if player_y < obstacle2_y + obstacle2_height and player_y + player_height > obstacle2_y:
            running = False

    # Respawn the obstacles if timer reaches zero
    current_time = pygame.time.get_ticks()
    if current_time - obstacle_timer >= obstacle_respawn_time:
        obstacle_x = screen_width
        obstacle_y = random.randint(0, screen_height - obstacle_height)

        obstacle2_x = random.randint(0, screen_width - obstacle2_width)
        obstacle2_y = screen_height
        obstacle2_direction = random.choice([-1, 1])

        obstacle_timer = current_time

    # Update the display
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, WHITE, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    pygame.draw.rect(screen, WHITE, (obstacle2_x, obstacle2_y, obstacle2_width, obstacle2_height))
    pygame.display.update()

    clock.tick(60)

# Quit the game
pygame.quit()
