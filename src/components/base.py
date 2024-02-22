import pygame

from .constants import *

def load_button_image(path: str):
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(image, (BUTTON_WIDTH, BUTTON_HEIGHT))


def draw_button(screen, button_rect, image):
    screen.blit(image, button_rect)
