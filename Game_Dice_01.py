# 1402-03-19
# Hamid Reza Komeylian

import pygame
import random

pygame.init()

width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Random Dice Game")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 100)  # Choose the desired font and size


def roll_dice():
    dice_face = random.randint(1, 6)
    # Render the dice face as text
    text = font.render(str(dice_face), True, (0, 0, 0))
    # Center the text on the screen
    text_rect = text.get_rect(center=(width/2, height/2))
    screen.fill((255, 255, 255))
    screen.blit(text, text_rect)
    pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                roll_dice()

    clock.tick(30)

pygame.quit()
