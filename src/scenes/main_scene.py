from components.base import *
from components.widgets import *
from components.constants import *


def create_title():
    global CURRENT_LANGUAGE, MESSAGES
    return Title(int(FONT_SIZE * 1.5), COLORS["WHITE"], WIDTH // 2, MARGIN, MESSAGES[CURRENT_LANGUAGE]["TITLE"])


def create_buttons():
    yes_button = YesButton()
    no_button = NoButton()
    return yes_button, no_button


def create_interactive_text(no_button):
    global CURRENT_LANGUAGE, MESSAGES
    return InteractiveText(int(FONT_SIZE * 0.9), COLORS["WHITE"], WIDTH // 2 - BUTTON_WIDTH // 2, HEIGHT // 2 + MARGIN // 4, no_button, MESSAGES[CURRENT_LANGUAGE]["NO"]["TIP"])


def main_scene():
    title = create_title()
    yes_button, no_button = create_buttons()
    interactive_text = create_interactive_text(no_button)
    return title, yes_button, no_button, interactive_text
