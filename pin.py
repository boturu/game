import pygame
import sys

# Initialize Pygame
pygame.init()

# Load sound
music = pygame.mixer.Sound("music.mp3")

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Define colors
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# Create rectangles
fixedRect1 = pygame.Rect(600, 400, 50, 80)
fixedRect2 = pygame.Rect(800, 400, 50, 80)
fixedRect3 = pygame.Rect(400, 400, 50, 80)
fixedRect4 = pygame.Rect(200, 400, 50, 80)
movingRect = pygame.Rect(400, 200, 80, 30)
car = pygame.Rect(200, 200, 30, 30)

# Set colors for rectangles
fixedRect1_color = green
fixedRect2_color = red
fixedRect3_color = blue
fixedRect4_color = yellow
movingRect_color = white
car_color = red

# Initialize car velocity
car_velocity_x = 5

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update moving rectangle position
    movingRect.x, movingRect.y = pygame.mouse.get_pos()

    # Check for collision
    if movingRect.colliderect(car):
        font = pygame.font.Font(None, 74)
        text = font.render("you win", True, white)
        screen.blit(text, (400, 600))

    # Update car position
    car.x += car_velocity_x

    # Bounce off walls
    if car.x > 800 or car.x < 0:
        car_velocity_x = -car_velocity_x

    # Clear screen
    screen.fill(black)

    # Draw rectangles
    pygame.draw.rect(screen, fixedRect1_color, fixedRect1)
    pygame.draw.rect(screen, fixedRect2_color, fixedRect2)
    pygame.draw.rect(screen, fixedRect3_color, fixedRect3)
    pygame.draw.rect(screen, fixedRect4_color, fixedRect4)
    pygame.draw.rect(screen, movingRect_color, movingRect)
    pygame.draw.rect(screen, car_color, car)

    # Update display
    pygame.display.flip()

