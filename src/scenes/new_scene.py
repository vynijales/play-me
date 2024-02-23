from components.base import *
from components.widgets import *
from components.constants import *


def new_scene():
    confirm_text = ConfirmText(int(FONT_SIZE * 1.5), COLORS["BLACK"], WIDTH // 2, HEIGHT //
                               2 + BUTTON_HEIGHT * 2, MESSAGES[CURRENT_LANGUAGE]["CONFIRM"],)

     
    last_chance = LastChanceText(FONT_SIZE, COLORS["BLACK"],
                 WIDTH // 2, HEIGHT // 2 + BUTTON_HEIGHT * 2, MESSAGES[CURRENT_LANGUAGE]["LAST"])

    confirm_button = ConfirmButton()
    back_button = BackButton()

    return last_chance, confirm_text, confirm_button, back_button
