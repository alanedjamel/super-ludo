import pygame
import os
import time
from mode_selection import show_mode_selection

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("assets/images/bg.jpg").convert()
        self.background = pygame.transform.scale(self.background, self.screen.get_size())
        self.hover_animation_start = time.time()

        self.buttons = [
            ("VS COMPUTER", (255, 255, 255), (90, 200)),
            ("LOCAL MULTIPLAYER", (255, 255, 255), (90, 270)),
            ("SETTING", (255, 255, 255), (90, 340)),
            ("EXIT", (255, 255, 255), (90, 410))
        ]

        self.logo = pygame.image.load("assets/images/logo.png")
        self.logo = pygame.transform.scale(self.logo, (220, 100))

        self.font = pygame.font.SysFont("comicsansms", 24, bold=True)

        self.icons = {
            "VS COMPUTER": pygame.image.load("assets/icons/competition.png"),
            "LOCAL MULTIPLAYER": pygame.image.load("assets/icons/multi-users.png"),
            "SETTING": pygame.image.load("assets/icons/setting.png"),
            "EXIT": pygame.image.load("assets/icons/exit.png")
        }

        for key in self.icons:
            self.icons[key] = pygame.transform.scale(self.icons[key], (32, 32))

        self.hovered_button = None
        self.clock = pygame.time.Clock()

    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        previous_hover = self.hovered_button
        self.hovered_button = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for text, _, (bx, by) in self.buttons:
                    rect = pygame.Rect(bx, by, 240, 50)
                    if rect.collidepoint(mouse_pos):
                        if text == "VS COMPUTER":
                            show_mode_selection(self.screen)
                        elif text == "EXIT":
                            pygame.quit()
                            exit()

        for text, _, (bx, by) in self.buttons:
            if pygame.Rect(bx, by, 240, 50).collidepoint(mouse_pos):
                self.hovered_button = text
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                break
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        if self.hovered_button != previous_hover:
            self.hover_animation_start = time.time()

    def draw_button(self, text, color, pos, is_hovered):
        x, y = pos
        button_width, button_height = 240, 50
        scale = 1.1 if is_hovered else 1.0
        draw_width = int(button_width * scale)
        draw_height = int(button_height * scale)
        draw_x = x - (draw_width - button_width) // 2

        offset_y = int(5 * pygame.math.sin((time.time() - self.hover_animation_start) * 6)) if is_hovered else 0
        draw_y = y - (draw_height - button_height) // 2 + offset_y

        base_color = (100, 170, 220) if is_hovered else (70, 130, 180)
        border_color = (255, 255, 255) if is_hovered else (0, 0, 0)

        # Ombre
        pygame.draw.rect(self.screen, (0, 0, 0, 50), (draw_x + 3, draw_y + 3, draw_width, draw_height), border_radius=12)
        # Fond
        pygame.draw.rect(self.screen, base_color, (draw_x, draw_y, draw_width, draw_height), border_radius=12)
        # Bord
        pygame.draw.rect(self.screen, border_color, (draw_x, draw_y, draw_width, draw_height), 2, border_radius=12)

        # Texte + Icône
        label = self.font.render(text, True, color)
        label_width, label_height = label.get_size()
        icon = self.icons.get(text)
        icon_width = icon.get_width() if icon else 0
        spacing = 10 if icon else 0

        total_width = icon_width + spacing + label_width
        start_x = draw_x + (draw_width - total_width) // 2
        center_y = draw_y + (draw_height - label_height) // 2

        if icon:
            self.screen.blit(icon, (start_x, draw_y + (draw_height - icon.get_height()) // 2))
            start_x += icon_width + spacing

        self.screen.blit(label, (start_x, center_y))

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.logo, (self.screen.get_width() // 2 - self.logo.get_width() // 2, 60))

        for text, color, pos in self.buttons:
            self.draw_button(text, color, pos, is_hovered=(text == self.hovered_button))

        pygame.display.flip()
        self.clock.tick(60)
