from components.base import *
from components.widgets import *
from components.constants import *

def main_scene():
    title = Title(int(FONT_SIZE * 1.5), COLORS["WHITE"], WIDTH // 2, HEIGHT // 2 - 2 * BUTTON_HEIGHT, MASSAGES[CURRENT_LANGUAGE]["TITLE"])

    yes_button = YesButton()
    no_button = NoButton()

    br_button = BRButton()
    fr_button = FRButton()
    uk_button = UKButton()
    es_button = ESButton()
    kr_button = KRButton()


    interactive_text = InteractiveText(int(FONT_SIZE * 0.8), COLORS["WHITE"],
                                      WIDTH // 2, HEIGHT // 2 + 2 * BUTTON_HEIGHT, no_button, MASSAGES[CURRENT_LANGUAGE]["NO"]["TIP"])

    return title, yes_button, no_button, interactive_text, br_button, fr_button, uk_button, es_button, kr_button
