from components.base import *
from components.widgets import *
from components.constants import *
import random


def last_scene():
    love_text = LoveYouText(
        FONT_SIZE * 2, COLORS["DARK PURPLE"], WIDTH // 2, MARGIN // 2)

    image = Image(resource_path("assets/image/vaso.png"), (300, 300), WIDTH // 2, HEIGHT // 2)

    return love_text, image
