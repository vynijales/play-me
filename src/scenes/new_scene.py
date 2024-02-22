from components.base import *
from components.widgets import *
from components.constants import *

def new_scene():
    title = Text("NEW SCENE",
                 FONT_SIZE, COLORS["BLACK"],
                 WIDTH // 2, HEIGHT // 2)

    back_button = BackButton()

    return title, back_button