# gestion des jouers
import pygame

class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.position = (0, 0)  # Position initiale
        self.image = pygame.image.load(f'assets/images/pion{player_id + 1}.png')  # Charger l'image du pion

    def move(self, steps):
        # Logique pour déplacer le pion
        # Mettez à jour la position en fonction de `steps`
        self.position = (self.position[0] + steps * 70, self.position[1])  # Exemple simple

    def draw(self, screen):
        screen.blit(self.image, self.position)  # Dessiner le pion