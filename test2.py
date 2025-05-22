import pygame
import random
import os

class Dice:
    def __init__(self):
        self.value = 1
        self.size = 60
        self.position = (390, 560)
        self.update_rect()
        self.border_radius = 12  # coins arrondis

    def roll(self):
        self.value = random.randint(1, 6)
        self.update_rect()

    def update_rect(self):
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size, self.size)

    def draw_dots(self, surface, rect=None):
        if rect is None:
            rect = self.rect
        cx, cy = rect.center
        offset = 12
        radius = 5
        positions = {
            1: [(cx, cy)],
            2: [(cx - offset, cy - offset), (cx + offset, cy + offset)],
            3: [(cx, cy), (cx - offset, cy - offset), (cx + offset, cy + offset)],
            4: [(cx - offset, cy - offset), (cx + offset, cy - offset),
                (cx - offset, cy + offset), (cx + offset, cy + offset)],
            5: [(cx, cy), (cx - offset, cy - offset), (cx + offset, cy - offset),
                (cx - offset, cy + offset), (cx + offset, cy + offset)],
            6: [(cx - offset, cy - offset), (cx + offset, cy - offset),
                (cx - offset, cy), (cx + offset, cy),
                (cx - offset, cy + offset), (cx + offset, cy + offset)],
        }
        for x, y in positions[self.value]:
            pygame.draw.circle(surface, (0, 0, 0), (x, y), radius)

    def draw(self, surface, rect=None):
        if rect is None:
            rect = self.rect
        pygame.draw.rect(surface, (255, 255, 255), rect, border_radius=self.border_radius)
        pygame.draw.rect(surface, (0, 0, 0), rect, 2, border_radius=self.border_radius)
        self.draw_dots(surface, rect)


class Board:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen_width = 900
        self.screen_height = 720
        self.cell_size = 80
        self.cols = 9
        self.rows = 6
        self.margin_top = 100
        self.margin_left = 50

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Super Ludo - Plateau de jeu avec dé")

        self.dice = Dice()

        # Charger son du dé
        self.dice_sound = None
        if os.path.exists("dice.mp3"):
            self.dice_sound = pygame.mixer.Sound("dice.mp3")
        else:
            print("Warning: fichier 'dice_roll.wav' non trouvé, son désactivé.")

        self.custom_bg_cells = {
            (1, 2): (200, 255, 100),
            (2, 4): (200, 255, 100),
            (3, 0): (200, 255, 100),
            (4, 3): (200, 255, 100),
            (1, 1): (255, 150, 150),
            (3, 2): (255, 150, 150),
            (5, 5): (255, 150, 150)
        }

    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.cell_size + self.margin_left
                y = row * self.cell_size + self.margin_top
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                color = self.custom_bg_cells.get((col, row), (220, 220, 220))
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

    def draw_dice_area(self):
        rect = pygame.Rect(360, 550, 180, 80)
        pygame.draw.rect(self.screen, (100, 200, 250), rect, border_radius=15)
        pygame.draw.rect(self.screen, (0, 0, 0), rect, 2, border_radius=15)
        font = pygame.font.SysFont(None, 28)
        label = font.render(" ", True, (0, 0, 0))
        self.screen.blit(label, (rect.x + 40, rect.y + 25))

    def draw(self):
        self.screen.fill((240, 240, 240))
        self.draw_grid()
        self.draw_dice_area()
        self.dice.draw(self.screen)
        pygame.display.flip()

    def roll_dice_with_3d_effect(self):
        # Jouer son si dispo
        if self.dice_sound:
            self.dice_sound.play()

        clock = pygame.time.Clock()
        duration_ms = 600
        elapsed = 0

        orig_rect = self.dice.rect.copy()

        while elapsed < duration_ms:
            elapsed += clock.tick(60)
            # Effet 3D: on oscille la largeur du dé entre 100% et 50%
            # On calcule un facteur selon le temps avec sin pour effet fluide
            import math
            factor = 0.5 + 0.5 * math.sin( (elapsed / duration_ms) * math.pi * 4 )  # 4 oscillations
            new_width = int(orig_rect.width * (0.5 + 0.5 * factor))
            new_width = max(20, new_width)

            # Centrer horizontalement
            new_x = orig_rect.centerx - new_width // 2
            new_rect = pygame.Rect(new_x, orig_rect.y, new_width, orig_rect.height)

            # On dessine
            self.screen.fill((240, 240, 240))
            self.draw_grid()
            self.draw_dice_area()
            # On dessine le dé compressé
            self.dice.draw(self.screen, new_rect)
            pygame.display.flip()

        # À la fin, lancer le dé normalement
        self.dice.roll()
        self.draw()

if __name__ == '__main__':
    board = Board()
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if board.dice.rect.collidepoint(event.pos):
                    board.roll_dice_with_3d_effect()

        board.draw()
        clock.tick(30)

    pygame.quit()
