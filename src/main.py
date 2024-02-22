import pygame
from pygame.font import Font

from components.base import *
from components.widgets import *
from components.constants import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PLAY ME")

# DO YOU WANNA BE MY GIRLFRIEND?
title = Text("A SIMPLE QUESTION",
             FONT_SIZE, COLORS["BLACK"],
             WIDTH // 2, HEIGHT // 2 - 2 * BUTTON_HEIGHT)

yes_button = YesButton()
no_button = NoButton()

interactive_text = InteractiveText(int(FONT_SIZE * 0.8), COLORS["WHITE"],
                                  WIDTH // 2, HEIGHT // 2 + 2 * BUTTON_HEIGHT, no_button, MASSAGES["NO"]["TIP"])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            no_button.update(event)
            yes_button.update(event)

    screen.fill(COLORS["GHOST WHITE"])

    title.draw(screen)

    no_button.draw(screen)
    yes_button.draw(screen)

    interactive_text.draw(screen)

    pygame.display.flip()

pygame.quit()