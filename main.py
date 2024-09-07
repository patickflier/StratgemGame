import pygame

# init pygame setup
pygame.init()
HEIGHT, WIDTH = 800, 800
BACKGROUND_COLOR = (169, 169, 169)
screen = pygame.display.set_mode((HEIGHT, WIDTH))
running = True

while running:
    screen.fill(BACKGROUND_COLOR)
    pygame.display.update()

pygame.quit()

