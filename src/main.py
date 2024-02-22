import pygame
from pygame.font import Font

from components.base import *
from components.widgets import *
from components.constants import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PLAY ME")

title = Text("DO YOU WANNA BE MY GIRLFRIEND?",
             FONT_SIZE, COLORS["BLACK"],
             WIDTH // 2, HEIGHT // 2 - 2 * BUTTON_HEIGHT)

yes_button = YesButton()
no_button = NoButton()

interactive_text = InteractiveText("I think you're trying to press the wrong button",
                                  int(FONT_SIZE * 0.8), COLORS["WHITE"],
                                  WIDTH // 2, HEIGHT // 2 + 2 * BUTTON_HEIGHT, no_button, 5)

interactive_text2 = InteractiveText("Ok... I'll help you",
                                    int(FONT_SIZE * 0.8), COLORS["WHITE"],
                                    WIDTH // 2, HEIGHT // 2 + 2 * BUTTON_HEIGHT + 20, no_button, 10, True)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            no_button.update(event)

    screen.fill(COLORS["GHOST WHITE"])

    title.draw(screen)

    yes_button.draw(screen)
    no_button.draw(screen)

    interactive_text.draw(screen)
    interactive_text2.draw(screen)

    pygame.display.flip()

pygame.quit()