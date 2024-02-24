import pygame
from pygame.font import Font

from components.base import *
from components.widgets import *
from components.constants import *

from scenes.main_scene import main_scene
from scenes.new_scene import new_scene
from scenes.first_scene import first_scene
from scenes.last_scene import last_scene


def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PLAY ME")
    pygame.font.init()

    pygame.mixer.music.load(resource_path("assets/sound/love.mp3"))
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0)

    # Estado atual da cena
    current_scene = "first_scene"
    
    # Cenas
    SCENES = {
        "first_scene": first_scene(),
        "main_scene": main_scene(),
        "new_scene": new_scene(),
        "last_scene": last_scene(),
    }

    language_buttons = [BRButton(), FRButton(), UKButton(),
                        ESButton(), KRButton()]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if current_scene == "last_scene" or current_scene == "first_scene":
                    running = False

            if current_scene == "main_scene":
                for i in range(4):
                    SCENES["main_scene"][i].update(event)
                    SCENES["main_scene"][i].update(event)

            elif current_scene == "new_scene":
                for i in range(4):
                    SCENES["new_scene"][i].update(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in language_buttons:
                    button.update(event)

        screen.fill(COLORS["GHOST WHITE"])

        if current_scene == "main_scene":
            for i in range(4):
                SCENES["main_scene"][i].draw(screen)

            if SCENES["main_scene"][1].clicked:
                SCENES["main_scene"][1].clicked = False
                current_scene = "last_scene"

        elif current_scene == "new_scene":
            for i in range(4):
                SCENES["new_scene"][i].draw(screen)

            if SCENES["new_scene"][2].clicked:
                SCENES["new_scene"][2].clicked = False
                current_scene = "last_scene"

            if SCENES["new_scene"][3].clicked:
                SCENES["new_scene"][3].clicked = False
                current_scene = "main_scene"

        elif current_scene == "first_scene":
            if pygame.time.get_ticks() > 5000:
                current_scene = "main_scene"

            SCENES["first_scene"].update(event)
            SCENES["first_scene"].draw(screen)

        elif current_scene == "last_scene":
            for i in range(2):
                SCENES["last_scene"][i].update(event)
                SCENES["last_scene"][i].draw(screen)

        for button in language_buttons:
            button.update(event)
            button.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
