import pygame

# init pygame setup
pygame.init()
HEIGHT, WIDTH = 800, 800
BACKGROUND_COLOR = (169, 169, 169)
screen = pygame.display.set_mode((HEIGHT, WIDTH))
running = True

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()


while running:
    screen.fill(BACKGROUND_COLOR)
    quit_game()
    pygame.display.update()

pygame.quit()

