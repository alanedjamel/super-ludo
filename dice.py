import pygame
import random

class Dice:
    def __init__(self):
        self.value = 1
        self.font = pygame.font.SysFont("Arial", 48)
        self.size = 70  # Taille du dé
        self.position = (600, 100)  # Position par défaut (modifiable)
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size, self.size)

    def roll(self):
        self.value = random.randint(1, 6)  # Lancer le dé

    def update_rect(self):
        # Recréation du rect pour bien prendre en compte la position et la taille
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size, self.size)

    def draw(self, screen):
        # Couleurs
        BLUE = (0, 0, 255)
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)

        # Fond bleu avec bord arrondi
        pygame.draw.rect(screen, BLUE, self.rect, border_radius=15)

        # Dessiner les points
        self.draw_dots(screen)

        # Optionnel : afficher la valeur en chiffre blanc au centre (si tu veux)
        # text = self.font.render(str(self.value), True, WHITE)
        # text_rect = text.get_rect(center=self.rect.center)
        # screen.blit(text, text_rect)

    def draw_dots(self, screen):
        # Positions des points sur le dé (relatives à self.position)
        dot_positions = {
            1: [(self.position[0] + self.size // 2, self.position[1] + self.size // 2)],
            2: [
                (self.position[0] + 20, self.position[1] + 20),
                (self.position[0] + self.size - 20, self.position[1] + self.size - 20)
            ],
            3: [
                (self.position[0] + self.size // 2, self.position[1] + self.size // 2),
                (self.position[0] + 20, self.position[1] + 20),
                (self.position[0] + self.size - 20, self.position[1] + self.size - 20)
            ],
            4: [
                (self.position[0] + 20, self.position[1] + 20),
                (self.position[0] + 20, self.position[1] + self.size - 20),
                (self.position[0] + self.size - 20, self.position[1] + 20),
                (self.position[0] + self.size - 20, self.position[1] + self.size - 20)
            ],
            5: [
                (self.position[0] + 20, self.position[1] + 20),
                (self.position[0] + 20, self.position[1] + self.size - 20),
                (self.position[0] + self.size - 20, self.position[1] + 20),
                (self.position[0] + self.size - 20, self.position[1] + self.size - 20),
                (self.position[0] + self.size // 2, self.position[1] + self.size // 2)
            ],
            6: [
                (self.position[0] + 20, self.position[1] + 20),
                (self.position[0] + 20, self.position[1] + self.size // 2),
                (self.position[0] + 20, self.position[1] + self.size - 20),
                (self.position[0] + self.size - 20, self.position[1] + 20),
                (self.position[0] + self.size - 20, self.position[1] + self.size // 2),
                (self.position[0] + self.size - 20, self.position[1] + self.size - 20)
            ]
        }
        for pos in dot_positions[self.value]:
            pygame.draw.circle(screen, (0, 0, 0), pos, 10)
