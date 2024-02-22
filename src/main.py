import pygame

from components.base import *
from components.widgets import *
from components.constants import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PLAY ME")


def main():
    title = Text("DO YOU WANNA BE MY GIRLFRIEND?",
                 FONT_SIZE, COLORS["BLACK"],
                 WIDTH // 2, HEIGHT // 2 - 2 * BUTTON_HEIGHT)

    yes_button = YesButton()
    no_button = NoButton()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                no_button.update(event)

        screen.fill(COLORS["GHOST WHITE"])

        title.draw(screen)

        no_button.draw(screen)
        yes_button.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
