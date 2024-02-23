import pygame
import random

from .constants import *

COUNTER = 0
CURRENT_LANGUAGE = random.choice(["BR", "UK", "FR",  "ES"])

def load_button_image(path: str, scale = (BUTTON_WIDTH, BUTTON_HEIGHT)):
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(image, scale)


def draw_button(screen, button_rect, image):
    screen.blit(image, button_rect)
