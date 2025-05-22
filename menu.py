import pygame
import os
from PIL import Image
from mode_selection import show_mode_selection


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load("assets/images/bg.jpg").convert()
        self.background = pygame.transform.scale(self.background, self.screen.get_size())

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

        # Optionnel : redimensionner toutes les icônes
        for key in self.icons:
            self.icons[key] = pygame.transform.scale(self.icons[key], (32, 32))


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for text, _, (bx, by) in self.buttons:
                    button_rect = pygame.Rect(bx, by, 240, 50)
                    if button_rect.collidepoint((x, y)):
                        if text == "VS COMPUTER":
                            show_mode_selection(self.screen)
    

    def draw(self):
        self.screen.blit(self.background, (0, 0))


        # Draw Logo
        self.screen.blit(self.logo, (self.screen.get_width() // 2 - self.logo.get_width() // 2, 60))

        # Draw buttons
        for text, color, (x, y) in self.buttons:
            button_width, button_height = 240, 50
            pygame.draw.rect(self.screen, (50, 100, 200), (x, y, button_width, button_height), border_radius=10)
            pygame.draw.rect(self.screen, (0, 0, 0), (x, y, button_width, button_height), 2, border_radius=10)

            # Rendu du texte
            label = self.font.render(text, True, color)
            label_width, label_height = label.get_size()

            # Icône (optionnelle)
            icon = self.icons.get(text)
            icon_width = icon.get_width() if icon else 0
            icon_height = icon.get_height() if icon else 0
            spacing = 10 if icon else 0  # espace entre icône et texte

            total_width = icon_width + spacing + label_width
            start_x = x + (button_width - total_width) // 2
            center_y = y + (button_height - label_height) // 2

            # Blit icon
            if icon:
                self.screen.blit(icon, (start_x, y + (button_height - icon_height) // 2))
                start_x += icon_width + spacing

            # Blit text
            self.screen.blit(label, (start_x, center_y))

            self.handle_events()



        pygame.display.flip()
