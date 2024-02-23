from components.base import *
from components.widgets import *
from components.constants import *
import random

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def last_scene():
    title = Text( "FERNANDA INACIO DE LIMA", int(FONT_SIZE * 1.5), COLORS["BLACK"], WIDTH // 2, MARGIN)
    title2 = LoveYouText(FONT_SIZE * 2, COLORS["DARK PURPLE"], WIDTH // 2 - MARGIN * 1.4, HEIGHT // 2 - MARGIN)

    lista = []

    return title, title2, lista