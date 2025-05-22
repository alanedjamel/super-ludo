# Gestion du plateau de jeu
import pygame

class Board:
    def __init__(self):
        self.start_position = (50, 50)  # Position du start
        self.images = {
            'machette': pygame.image.load('assets/images/—Pngtree—tapanga machete_5996414.png'),
            'pierre': pygame.image.load('assets/images/—Pngtree—large piece of mineral stone_4562686.png'),
            'couteau': pygame.image.load('assets/images/couteau.png'),
            'voiture': pygame.image.load('assets/images/voiture2.png'),
            'avion': pygame.image.load('assets/images/avion.png'),
            'metro': pygame.image.load('assets/images/metro.png'),
            'fusee': pygame.image.load('assets/images/fusee.png'),
            'head': pygame.image.load('assets/images/head fire.png')
        }
        self.advantages_positions = [(2, 3), (5, 5)]  # Exemples de positions pour avantages
        self.obstacles_positions = [(1, 1), (3, 4)]  # Exemples de positions pour obstacles
    def load_image(self, path):
        if os.path.exists(path):
            return pygame.image.load(path)
        else:
            print(f"Image non trouvée : {path}")
            return None

    def draw(self, screen):
        # Dessiner le point de départ
        start_image = pygame.image.load('assets/images/start.png')
        screen.blit(start_image, self.start_position)

        # Dessiner les avantages
        for pos in self.advantages_positions:
            image = self.images['pierre']  # Par exemple, utiliser l'image de la voiture
            screen.blit(image, (pos[0] * self.cell_size + self.start_position[0],
                                pos[1] * self.cell_size + self.start_position[1]))

        # Dessiner les obstacles
        for pos in self.obstacles_positions:
            image = self.images['machette']  # Par exemple, utiliser l'image de la machette
            screen.blit(image, (pos[0] * self.cell_size + self.start_position[0],
                                pos[1] * self.cell_size + self.start_position[1]))


        # Ajouter des flèches pour relier les éléments (à faire)