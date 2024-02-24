import pygame
import random
import os, sys

from .constants import *

COUNTER = 0
CURRENT_LANGUAGE = random.choice(["BR", "UK", "FR",  "ES", "KR"])


def load_button_image(path: str, scale=(BUTTON_WIDTH, BUTTON_HEIGHT)):
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(image, scale)


def draw_button(screen, button_rect, image):
    screen.blit(image, button_rect)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    # return relative_path
    return os.path.join(base_path, relative_path)
