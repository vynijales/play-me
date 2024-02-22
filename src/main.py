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

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                if current_scene == "main_scene":
                    SCENES["main_scene"][1].update(event)
                    SCENES["main_scene"][2].update(event)
                    SCENES["main_scene"][4].update(event)
                    SCENES["main_scene"][5].update(event)
                    SCENES["main_scene"][6].update(event)
                    SCENES["main_scene"][7].update(event)
                    SCENES["main_scene"][8].update(event)
                elif current_scene == "new_scene":
                    SCENES["new_scene"][1].update(event)

        screen.fill(COLORS["GHOST WHITE"])

        if current_scene == "main_scene":
            SCENES["main_scene"][0].draw(screen)
            SCENES["main_scene"][1].draw(screen)
            SCENES["main_scene"][2].draw(screen)
            SCENES["main_scene"][3].draw(screen)
            SCENES["main_scene"][4].draw(screen)
            SCENES["main_scene"][5].draw(screen)
            SCENES["main_scene"][6].draw(screen)
            SCENES["main_scene"][7].draw(screen)
            SCENES["main_scene"][8].draw(screen)

            if SCENES["main_scene"][1].clicked:
                # Reset the variable clicked of the "yes" button
                SCENES["main_scene"][1].clicked = False
                current_scene = "new_scene"

        elif current_scene == "new_scene":
            SCENES["new_scene"][0].draw(screen)
            SCENES["new_scene"][1].draw(screen)

            if SCENES["new_scene"][1].clicked:
                # Reset the variable clicked of the "back" button
                SCENES["new_scene"][1].clicked = False
                current_scene = "main_scene"

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
