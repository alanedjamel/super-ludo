import pygame
import time
from menu import Menu

def show_splash(screen):
    pygame.init()
    logo = pygame.image.load("assets/images/logo.png")
    logo = pygame.transform.scale(logo, (300, 150))

    screen.fill((0, 0, 50))
    screen.blit(logo, (
        screen.get_width() // 2 - logo.get_width() // 2,
        screen.get_height() // 2 - logo.get_height() // 2
    ))
    pygame.display.flip()

    time.sleep(3)  # Affiche pendant 5 secondes

    # Affiche le menu principal après la page de chargement
    menu = Menu(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        menu.draw()
