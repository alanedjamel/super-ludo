import pygame
import os

def play_background_music(file_path="assets/audio/sound-k-117217.mp3", volume=0.5):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(-1)  # -1 pour jouer en boucle

def stop_background_music():
    if pygame.mixer.get_init():
        pygame.mixer.music.stop()

#couleur des joeurs

PLAYER_COLORS = {
    "Rouge": (255, 0, 0),
    "Vert": (0, 255, 0),
    "Bleu": (0, 0, 255),
    "Jaune": (255, 255, 0)
}

COLOR_TRANSLATION = {
    "red": "Rouge",
    "green": "Vert",
    "blue": "Bleu",
    "yellow": "Jaune"
}

