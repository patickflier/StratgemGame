import pygame


# init pygame setup


def main(running=True):
    while running:
        quit_game()


def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()


def game_screen():
    pygame.init()
    height, width = 800, 800
    background_color = (169, 169, 169)
    screen = pygame.display.set_mode((height, width))
    screen.fill(background_color)
    pygame.display.update()
    return screen


if __name__ == "__main__":
    game_screen()
    main()
