from components.base import *
from components.widgets import *
from components.constants import *


def initial_scene():
    global MESSAGES
    initial_text = InitialText(FONT_SIZE * 2, COLORS["BLACK"], WIDTH // 2, HEIGHT //
                               2 + BUTTON_HEIGHT * 2, MESSAGES[CURRENT_LANGUAGE]["SALUTATION"])

    return initial_text
