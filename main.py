import pygame
from splash import show_splash

def main():
    pygame.init()
    screen = pygame.display.set_mode((480, 800))
    pygame.display.set_caption("Super Ludo")

    show_splash(screen)

    pygame.quit()

if __name__ == '__main__':
    main()
