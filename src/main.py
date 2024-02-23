import pygame
from pygame.font import Font

from components.base import *
from components.widgets import *
from components.constants import *

from scenes.main_scene import main_scene
from scenes.new_scene import new_scene


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PLAY ME")

    # Estado atual da cena
    current_scene = "main_scene"

    # Cenas
    SCENES = {
        "main_scene": main_scene(),
        "new_scene": new_scene()
    }

    language_buttons = [BRButton(), FRButton(), UKButton(), ESButton(), KRButton()]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if current_scene != "main_scene":
                    running = False
            else:
                if current_scene == "main_scene":
                    for i in range(1, 4):
                        SCENES["main_scene"][i].update(event)
                elif current_scene == "new_scene":
                    SCENES["new_scene"][2].update(event)
                    SCENES["new_scene"][3].update(event)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in language_buttons:
                    button.update(event)

        screen.fill(COLORS["GHOST WHITE"])

        if current_scene == "main_scene":
            for i in range(4):
                SCENES["main_scene"][i].draw(screen)

            if SCENES["main_scene"][1].clicked:
                # Reset the variable clicked of the "yes" button
                SCENES["main_scene"][1].clicked = False
                current_scene = "new_scene"

        elif current_scene == "new_scene":
            for i in range(4):
                SCENES["new_scene"][i].draw(screen)

            if SCENES["new_scene"][3].clicked:
                # Reset the variable clicked of the "back" button
                SCENES["new_scene"][3].clicked = False
                current_scene = "main_scene"
                print("Back to main scene")

        for button in language_buttons:
            button.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
