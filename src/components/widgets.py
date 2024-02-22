## Widgets
import random

from .base import *
from .constants import *

class Button:
    def __init__(self, image, rect):
        self.image = image
        self.rect = rect

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class YesButton(Button):
    def __init__(self):
        image = load_button_image("assets/YES.png")
        rect = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2 - MARGIN, HEIGHT // 2 - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
        super().__init__(image, rect)


class NoButton(Button):
    def __init__(self):
        self._contador = 0
        self.disable = False
        image = load_button_image("assets/NO.png")
        rect = pygame.Rect(WIDTH // 2 - BUTTON_WIDTH // 2 + MARGIN, HEIGHT // 2 - BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT)
        super().__init__(image, rect)

    def update(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.rect.x, self.rect.y = random.randint(0, WIDTH - BUTTON_WIDTH), random.randint(0, HEIGHT - BUTTON_HEIGHT)
                self._contador += 1

    def set_disable(self):
        self.image = load_button_image("assets/NO_DISABLE.png")

    def get_out(self):
        self.rect.x, self.rect.y = -500, -500

    def get_contador(self):
        return self._contador

class Text:
    def __init__(self, text, font_size, color, x, y):
        self.font = pygame.font.Font(None, font_size)
        self.text = self.font.render(text, True, color)
        self.rect = self.text.get_rect(center=(x, y))
        self.massage = text

    def draw(self, screen):
        screen.blit(self.text, self.rect)

class InteractiveText(Text):
    def __init__(self, text, font_size, color, x, y, object, min_contador=10, disable=False):
        super().__init__(text, font_size, color, x, y)
        self.object = object
        self.min_contador = min_contador
        self.disable = disable

    def draw(self, screen):
        if self.object.get_contador() >= self.min_contador:
            self.text = self.font.render(self.massage, True, COLORS["BLACK"])
            screen.blit(self.text, self.rect)
            self.object.set_disable()

            if self.disable and self.object.get_contador() >= self.min_contador + 5:
                self.object.get_out()