import pygame
import random
import math
import os

class Dice:
    def __init__(self):
        self.value = 1
        self.size = 50
        self.position = (390, 560)
        self.update_rect()
        self.border_radius = 12

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
    def __init__(self, screen):
        self.screen = screen
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        self.screen_width = 900
        self.screen_height = 720
        self.cell_size = 80
        self.cols = 10
        self.rows = 6
        self.margin_top = 50
        self.margin_left = 50

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Super Ludo")

        self.dice = Dice()
        self.images = self.load_images()

        if os.path.exists("assets/song/dice.mp3"):
            self.dice_sound = pygame.mixer.Sound("assets/song/dice.mp3")
        else:
            self.dice_sound = None
            print("Son du dé non trouvé.")

        self.advantages_positions = {
            (6, 0): 'voiture',
            (0, 4): 'avion',
            (1, 5): 'metro',
            (4, 3): 'fusee'
        }
        self.obstacles_positions = {
            (8, 3): 'machete',
            (3, 4): 'pierre',
            (6, 2): 'couteau',
            (9, 4): 'head'
        }
        self.connections = [
            ((0, 4), (2, 0)),
            ((1, 5), (3, 2)),
            ((4, 3), (6, 0)),
            ((6, 0), (8, 1)),
            ((8, 3), (4, 5)),
            ((6, 2), (3, 0)),
            ((9, 4), (3, 4)),
            ((3, 4), (0, 0))

        ]
        self.custom_bg_cells = {
            (0, 4): (37, 10, 156), #avion
            (1, 5): (101, 4, 192), #metro
            (3, 4): (18, 8, 59),   #stone
            (4, 3): (200, 255, 100), #fusee
            (6, 2): (255, 150, 150), #couteau
            (8, 3): (6, 3, 180),     #machette
            (9, 4): (0, 0, 0),       #head fire
            (6, 0): (248, 7, 7)      #voiture
        }

    def load_images(self):
        base_path = 'assets/images'
        image_files = {
            'machete': 'machete.png',
            'pierre': '—Pngtree—large piece of mineral stone_4562686.png',
            'couteau': 'couteau.png',
            'voiture': 'voiture2.png',
            'avion': 'avion.png',
            'metro': 'metro.png',
            'fusee': 'fusee.png',
            'start': 'start.png',
            'head' :  'head fire.png'
        }
        images = {}
        for name, file in image_files.items():
            path = os.path.join(base_path, file)
            if os.path.exists(path):
                img = pygame.image.load(path).convert_alpha()
                img = pygame.transform.scale(img, (self.cell_size, self.cell_size))
                images[name] = img
            else:
                print(f"Image non trouvée : {path}")
        return images

    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.cell_size + self.margin_left
                y = row * self.cell_size + self.margin_top
                rect = pygame.Rect(x, y, self.cell_size, self.cell_size)
                color = self.custom_bg_cells.get((col, row), (220, 220, 220))
                pygame.draw.rect(self.screen, color, rect)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

    def draw_elements(self):
        start_img = self.images.get('start')
        if start_img:
            x = 0 * self.cell_size + self.margin_left
            y = 0 * self.cell_size + self.margin_top
            self.screen.blit(start_img, (x, y))
        for pos, name in self.advantages_positions.items():
            image = self.images.get(name)
            if image:
                x = pos[0] * self.cell_size + self.margin_left
                y = pos[1] * self.cell_size + self.margin_top
                self.screen.blit(image, (x, y))

        for pos, name in self.obstacles_positions.items():
            image = self.images.get(name)
            if image:
                x = pos[0] * self.cell_size + self.margin_left
                y = pos[1] * self.cell_size + self.margin_top
                self.screen.blit(image, (x, y))

    def draw_arrows(self):
        for start, end in self.connections:
            sx = start[0] * self.cell_size + self.cell_size // 2 + self.margin_left
            sy = start[1] * self.cell_size + self.cell_size // 2 + self.margin_top
            ex = end[0] * self.cell_size + self.cell_size // 2 + self.margin_left
            ey = end[1] * self.cell_size + self.cell_size // 2 + self.margin_top
            pygame.draw.line(self.screen, (0, 0, 0), (sx, sy), (ex, ey), 3)

            angle = math.atan2(ey - sy, ex - sx)
            arrow_size = 10
            p1 = (ex, ey)
            p2 = (ex - arrow_size * math.cos(angle - math.pi / 6), ey - arrow_size * math.sin(angle - math.pi / 6))
            p3 = (ex - arrow_size * math.cos(angle + math.pi / 6), ey - arrow_size * math.sin(angle + math.pi / 6))
            pygame.draw.polygon(self.screen, (0, 0, 0), [p1, p2, p3])

    def draw_labels(self):
        font = pygame.font.SysFont("arial", 23)
        num = 1
        for col in range(self.cols):
            for row in range(self.rows):
                pos = (col, row)
                if pos == (0, 0):  # on ignore la cellule (0,0)
                    continue
                if pos in self.advantages_positions or pos in self.obstacles_positions:
                    continue
                x = col * self.cell_size + self.margin_left + self.cell_size // 2
                y = row * self.cell_size + self.margin_top + self.cell_size // 2
                text = font.render(str(num), True, (0, 0, 255))
                text_rect = text.get_rect(center=(x, y))
                self.screen.blit(text, text_rect)
                num += 1

    def draw_dice_area(self):
        rect = pygame.Rect(367, 555, 100, 60)
        pygame.draw.rect(self.screen, (100, 200, 250), rect, border_radius=15)
        pygame.draw.rect(self.screen, (0, 0, 0), rect, 2, border_radius=15)
        font = pygame.font.SysFont(None, 28)
        label = font.render(" ", True, (0, 0, 0))
        self.screen.blit(label, (rect.x + 40, rect.y + 25))

    def draw(self):
        self.screen.fill((240, 240, 240))
        self.draw_grid()
        self.draw_elements()
        self.draw_arrows()
        self.draw_labels()
        self.draw_dice_area()
        self.dice.draw(self.screen)
        pygame.display.flip()

    def roll_dice_with_animation(self):
        if self.dice_sound:
            self.dice_sound.play()

        clock = pygame.time.Clock()
        duration = 600
        elapsed = 0
        orig_rect = self.dice.rect.copy()

        while elapsed < duration:
            elapsed += clock.tick(60)
            factor = 0.5 + 0.5 * math.sin((elapsed / duration) * math.pi * 4)
            new_width = int(orig_rect.width * (0.5 + 0.5 * factor))
            new_width = max(20, new_width)
            new_x = orig_rect.centerx - new_width // 2
            new_rect = pygame.Rect(new_x, orig_rect.y, new_width, orig_rect.height)

            self.screen.fill((240, 240, 240))
            self.draw_grid()
            self.draw_elements()
            self.draw_arrows()
            self.draw_labels()
            self.draw_dice_area()
            self.dice.draw(self.screen, new_rect)
            pygame.display.flip()

        self.dice.roll()
        self.draw()

# if __name__ == '__main__':
#     board = Board()
#     clock = pygame.time.Clock()
#     running = True

#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if board.dice.rect.collidepoint(event.pos):
#                     board.roll_dice_with_animation()
#         board.draw()
#         clock.tick(30)

#     pygame.quit()
