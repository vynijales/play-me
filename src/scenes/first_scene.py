from components.base import *
from components.widgets import *
from components.constants import *


def first_scene():
    global MESSAGES, CURRENT_LANGUAGE
    initial_text = InitialText(FONT_SIZE * 2, COLORS["BLACK"], WIDTH // 2, HEIGHT //
                               2 + BUTTON_HEIGHT * 2, MESSAGES[CURRENT_LANGUAGE]["SALUTATION"])
    start_text = StartText(FONT_SIZE, COLORS["BLACK"], WIDTH // 2, HEIGHT //
                             2 + BUTTON_HEIGHT * 4, MESSAGES[CURRENT_LANGUAGE]["INITIAL"])
    return initial_text, start_text
