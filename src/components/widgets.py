# Widgets
import random

from .base import *
from .constants import *


class Button:
    def __init__(self, image, rect, hover_image=None, hover=False, text=""):
        self.image = image
        self.rect = rect
        self.hover_image = hover_image
        self.hover = hover
        self.text = text
        self.clicked = False

    def draw(self, screen):
        if self.hover and self.hover_image:
            screen.blit(self.hover_image, self.rect)
        else:
            screen.blit(self.image, self.rect)
        if self.text:
            font = pygame.font.SysFont("Arial", 16)
            text_surface = font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)



class YesButton(Button):
    def __init__(self):
        self.rect = pygame.Rect(
            WIDTH // 2 - BUTTON_WIDTH // 2 - MARGIN,
            HEIGHT // 2 - BUTTON_HEIGHT,
            BUTTON_WIDTH,
            BUTTON_HEIGHT
        )
        self.image = load_button_image("assets/YES.png")
        self.hover_image = load_button_image("assets/YES_HOVER.png")
        super().__init__(self.image, self.rect, self.hover_image)

    def draw(self, screen):
        if COUNTER >= CHECKPOINTS[2]:
            self.rect.x = WIDTH // 2 - BUTTON_WIDTH // 2

        if self.hover:
            screen.blit(self.hover_image, self.rect)
        else:
            screen.blit(self.image, self.rect)
        Text(MESSAGES[CURRENT_LANGUAGE]["YES"], FONT_SIZE, COLORS["WHITE"], self.rect.x + BUTTON_WIDTH // 2, self.rect.y + BUTTON_HEIGHT // 2).draw(screen)

    def update(self, event):
        global COUNTER

        if COUNTER == 0:
            self.rect.x = WIDTH // 2 - BUTTON_WIDTH // 2 - MARGIN

        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.hover = True
            else:
                self.hover = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                print(COUNTER)
                self.clicked = True


class NoButton(Button):
    def __init__(self):
        self.disable = False
        self.rect = pygame.Rect(
            WIDTH // 2 - BUTTON_WIDTH // 2 + MARGIN,
            HEIGHT // 2 - BUTTON_HEIGHT,
            BUTTON_WIDTH,
            BUTTON_HEIGHT
        )
        self.image = load_button_image("assets/NO.png")
        super().__init__(self.image, self.rect, text="NO")

    def update(self, event):
        global COUNTER
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.rect.x, self.rect.y = random.randint(
                    0, WIDTH - BUTTON_WIDTH), random.randint(0, HEIGHT - BUTTON_HEIGHT - 80)
                COUNTER = COUNTER + 1
        if COUNTER == 0:
            self.rect.x, self.rect.y = WIDTH // 2 - BUTTON_WIDTH // 2 + MARGIN, HEIGHT // 2 - BUTTON_HEIGHT
            self.image = load_button_image("assets/NO.png")

    def draw(self, screen):
        if self.hover:
            screen.blit(self.hover_image, self.rect)
            Text(MESSAGES[CURRENT_LANGUAGE]["NO"]["DEFAULT"], FONT_SIZE, COLORS["WHITE"], self.rect.x + BUTTON_WIDTH // 2, self.rect.y + BUTTON_HEIGHT // 2).draw(screen)
        else:
            screen.blit(self.image, self.rect)
            Text(MESSAGES[CURRENT_LANGUAGE]["NO"]["DEFAULT"], FONT_SIZE, COLORS["WHITE"], self.rect.x + BUTTON_WIDTH // 2, self.rect.y + BUTTON_HEIGHT // 2).draw(screen)

    def set_disable(self):
        self.image = load_button_image("assets/NO_DISABLE.png")

    def get_out(self):
        self.rect.x, self.rect.y = -500, -500


class ConfirmButton(Button):
    def __init__(self):
        self.rect = pygame.Rect(
            WIDTH // 2 - BUTTON_WIDTH // 2 - MARGIN,
            HEIGHT // 2 - BUTTON_HEIGHT,
            BUTTON_WIDTH,
            BUTTON_HEIGHT
        )
        self.image = load_button_image("assets/YES.png")
        self.hover_image = load_button_image("assets/YES_HOVER.png")
        super().__init__(self.image, self.rect, self.hover_image)

    def update(self, event):
        global COUNTER
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False
    
    def draw(self, screen):
        if self.hover:
            screen.blit(self.hover_image, self.rect)
        else:
            screen.blit(self.image, self.rect)
        
        Text(MESSAGES[CURRENT_LANGUAGE]["YES"], FONT_SIZE, COLORS["WHITE"], self.rect.x + BUTTON_WIDTH // 2, self.rect.y + BUTTON_HEIGHT // 2).draw(screen)


class BackButton(Button):
    def __init__(self):
        self.rect = pygame.Rect(
            WIDTH // 2 - BUTTON_WIDTH // 2 + MARGIN,
            HEIGHT // 2 - BUTTON_HEIGHT,
            BUTTON_WIDTH,
            BUTTON_HEIGHT
        )
        self.image = load_button_image("assets/NO.png")
        super().__init__(self.image, self.rect)

    def update(self, event):
        global COUNTER
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False
            COUNTER = 0

    def draw(self, screen):
        if self.hover:
            screen.blit(self.hover_image, self.rect)
            Text(MESSAGES[CURRENT_LANGUAGE]["NO"]["DEFAULT"], FONT_SIZE, COLORS["WHITE"], self.rect.x + BUTTON_WIDTH // 2, self.rect.y + BUTTON_HEIGHT // 2).draw(screen)
        else:
            screen.blit(self.image, self.rect)
            Text(MESSAGES[CURRENT_LANGUAGE]["NO"]["DEFAULT"], FONT_SIZE, COLORS["WHITE"], self.rect.x + BUTTON_WIDTH // 2, self.rect.y + BUTTON_HEIGHT // 2).draw(screen)


class LanguageButton:
    def __init__(self, rect, language):
        self.language = language
        self.image = load_button_image(f"assets/{language}.png", (LANGUAGE_WIDTH, LANGUAGE_HEIGHT))
        self.rect = rect
        self.clicked = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, event):
        global CURRENT_LANGUAGE
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.clicked = True
                CURRENT_LANGUAGE = self.language
        elif event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False


class BRButton(LanguageButton):
    def __init__(self):
        rect = pygame.Rect(WIDTH / 5 - LANGUAGE_WIDTH * 2, HEIGHT - MARGIN_FOOTER, LANGUAGE_WIDTH, LANGUAGE_HEIGHT)
        super().__init__(rect, "BR")


class FRButton(LanguageButton):
    def __init__(self):
        rect = pygame.Rect(WIDTH / 5 * 2 - LANGUAGE_WIDTH * 2, HEIGHT - MARGIN_FOOTER, LANGUAGE_WIDTH, LANGUAGE_HEIGHT)
        super().__init__(rect, "FR")


class UKButton(LanguageButton):
    def __init__(self):
        rect = pygame.Rect(WIDTH / 5 * 3 - LANGUAGE_WIDTH * 2, HEIGHT - MARGIN_FOOTER, LANGUAGE_WIDTH, LANGUAGE_HEIGHT)
        super().__init__(rect, "UK")


class ESButton(LanguageButton):
    def __init__(self):
        rect = pygame.Rect(WIDTH / 5 * 4 - LANGUAGE_WIDTH * 2, HEIGHT - MARGIN_FOOTER, LANGUAGE_WIDTH, LANGUAGE_HEIGHT)
        super().__init__(rect, "ES")


class KRButton(LanguageButton):
    def __init__(self):
        rect = pygame.Rect(WIDTH / 5 * 5 - LANGUAGE_WIDTH * 2, HEIGHT - MARGIN_FOOTER, LANGUAGE_WIDTH, LANGUAGE_HEIGHT)
        super().__init__(rect, "KR")


class Text:
    def __init__(self, text, font_size, color, x, y):
        self.font = pygame.font.Font(None, font_size)
        self.text = self.font.render(text, True, color)
        self.rect = self.text.get_rect(center=(x, y))
        self.massage = text

    def draw(self, screen):
        self.text = self.font.render(self.massage, True, COLORS["BLACK"])
        screen.blit(self.text, self.rect)

    def update(self, event):
        pass


class InitialText(Text):
    def __init__(self, font_size, color, x, y, text=""):
        super().__init__(text, font_size, color, x, y)

    def draw(self, screen):
        self.rect.x, self.rect.y = WIDTH // 2 - self.text.get_width() // 2, HEIGHT // 2 - self.text.get_height() // 2 - 10
        self.text = self.font.render(MESSAGES[CURRENT_LANGUAGE]["SALUTATION"], True, COLORS["BLACK"])
        screen.blit(self.text, self.rect)

class Title(Text):
    def __init__(self, font_size, color, x, y, text=""):
        super().__init__(text, font_size, color, x, y)

    def draw(self, screen):
        self.rect.x, self.rect.y = WIDTH // 2 - self.text.get_width() // 2, MARGIN // 2
        self.text = self.font.render(MESSAGES[CURRENT_LANGUAGE]["TITLE"], True, COLORS["BLACK"])
        screen.blit(self.text, self.rect)


class InteractiveText(Text):
    def __init__(self, font_size, color, x, y, object, text=""):
        super().__init__(text, font_size, color, x, y)
        self.object = object

    def draw(self, screen):
        global COUNTER

        self.rect.x = WIDTH // 2 - self.text.get_width() // 2
        self.rect.y = HEIGHT // 2 + 2 * BUTTON_HEIGHT

        if COUNTER == 0:
            self.text = self.font.render("", True, COLORS["WHITE"])

        if COUNTER >= CHECKPOINTS[2]:
            self.text = self.font.render(
                MESSAGES[CURRENT_LANGUAGE]["NO"]["END"], True, COLORS["BLACK"])
            self.object.get_out()

        elif COUNTER >= CHECKPOINTS[1]:
            self.text = self.font.render(
                MESSAGES[CURRENT_LANGUAGE]["NO"]["DISABLE"], True, COLORS["BLACK"])

        elif COUNTER >= CHECKPOINTS[0]:
            self.text = self.font.render(
                MESSAGES[CURRENT_LANGUAGE]["NO"]["TIP"], True, COLORS["BLACK"])
            self.object.set_disable()
        else:
            self.text = self.font.render("", True, COLORS["WHITE"])

        screen.blit(self.text, self.rect)


class ConfirmText(Text):
    def __init__(self, font_size, color, x, y, text=""):
        super().__init__(text, font_size, color, x, y)


    def draw(self, screen):
        self.rect.x, self.rect.y  = WIDTH // 2 - self.text.get_width() // 2, MARGIN // 2
        self.text = self.font.render(MESSAGES[CURRENT_LANGUAGE]["CONFIRM"], True, COLORS["BLACK"])
        screen.blit(self.text, self.rect)

class LastChanceText(Text):
    def __init__(self, font_size, color, x, y, text=""):
        super().__init__(text, font_size, color, x, y)

    def draw(self, screen):
        self.rect.x, self.rect.y = WIDTH // 2 - self.text.get_width() // 2, HEIGHT // 2 + 2 * BUTTON_HEIGHT
        self.text = self.font.render(MESSAGES[CURRENT_LANGUAGE]["LAST"], True, COLORS["BLACK"])
        screen.blit(self.text, self.rect)