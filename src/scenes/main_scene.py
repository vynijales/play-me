from components.base import *
from components.widgets import *
from components.constants import *

def main_scene():
    title = Text("A SIMPLE QUESTION",
                 FONT_SIZE, COLORS["BLACK"],
                 WIDTH // 2, HEIGHT // 2 - 2 * BUTTON_HEIGHT)

    yes_button = YesButton()
    no_button = NoButton()

    interactive_text = InteractiveText(int(FONT_SIZE * 0.8), COLORS["WHITE"],
                                      WIDTH // 2, HEIGHT // 2 + 2 * BUTTON_HEIGHT, no_button, MASSAGES["NO"]["TIP"])

    return title, yes_button, no_button, interactive_text
