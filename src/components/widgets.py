## Widgets
import random

from .base import *
from .constants import *

class Button:
    def __init__(self, image, rect, hover_image = None, hover = False):
        self.image = image
        self.hover_image = hover_image
        self.rect = rect
        self.hover = hover
        self.current = self.image

    def draw(self, screen):
        if self.hover:
            screen.blit(self.hover_image, self.rect)
        else:
            screen.blit(self.image, self.rect)


class YesButton(Button):
    def __init__(self):
        self.image = load_button_image("assets/YES.png")
        self.hover_image = load_button_image("assets/YES_HOVER.png")
        self.rect = pygame.Rect(
            WIDTH // 2 - BUTTON_WIDTH // 2 - MARGIN,
            HEIGHT // 2 - BUTTON_HEIGHT,
            BUTTON_WIDTH,
            BUTTON_HEIGHT
        )
        super().__init__(self.image, self.rect, self.hover_image)

    def draw(self, screen):
        if COUNTER >= CHECKPOINTS[2]:
            self.rect.x = WIDTH // 2 - BUTTON_WIDTH // 2
            
        return super().draw(screen)

    def update(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.hover = True
            else:
                self.hover = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print("YES")


class NoButton(Button):
    def __init__(self):
        self.disable = False
        self.image = load_button_image("assets/NO.png")
        self.rect = pygame.Rect(
            WIDTH // 2 - BUTTON_WIDTH // 2 + MARGIN,
            HEIGHT // 2 - BUTTON_HEIGHT,
            BUTTON_WIDTH,
            BUTTON_HEIGHT
        )
        super().__init__(self.image, self.rect)

    def update(self, event):
        global COUNTER
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.rect.x, self.rect.y = random.randint(0, WIDTH - BUTTON_WIDTH), random.randint(0, HEIGHT - BUTTON_HEIGHT)
                COUNTER = COUNTER + 1

    def set_disable(self):
        self.image = load_button_image("assets/NO_DISABLE.png")

    def get_out(self):
        self.rect.x, self.rect.y = -500, -500

class Text:
    def __init__(self, text, font_size, color, x, y):
        self.font = pygame.font.Font(None, font_size)
        self.text = self.font.render(text, True, color)
        self.rect = self.text.get_rect(center=(x, y))
        self.massage = text

    def draw(self, screen):
        screen.blit(self.text, self.rect)

class InteractiveText(Text):
    def __init__(self, font_size, color, x, y, object, text=""):
        super().__init__(text, font_size, color, x, y)
        self.object = object

    def draw(self, screen):
        global COUNTER

        self.rect.x = WIDTH // 2 - self.text.get_width() // 2
        self.rect.y = HEIGHT // 2 + 2 * BUTTON_HEIGHT

        if COUNTER >= CHECKPOINTS[2]:
            self.text = self.font.render(MASSAGES["NO"]["END"], True, COLORS["BLACK"])
            self.object.get_out()

        elif COUNTER >= CHECKPOINTS[1]:
            self.text = self.font.render(MASSAGES["NO"]["DISABLE"], True, COLORS["BLACK"])

        elif COUNTER >= CHECKPOINTS[0]:
            self.text = self.font.render(MASSAGES["NO"]["TIP"], True, COLORS["BLACK"])
            self.object.set_disable()
        else:
            self.text = self.font.render("", True, COLORS["WHITE"])

        screen.blit(self.text, self.rect)