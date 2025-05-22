import pygame
import sys

def show_classic_mode_settings(screen):
    pygame.init()
    width, height = screen.get_size()
    font = pygame.font.SysFont("comicsansms", 22, bold=True)
    small_font = pygame.font.SysFont("comicsansms", 18)

    selected_color = None
    selected_players = None

    running = True
    while running:
        screen.fill((0, 0, 0))

        # === Section couleur ===
        color_section = pygame.Rect(30, 80, width - 60, 180)
        pygame.draw.rect(screen, (74, 145, 158), color_section, border_radius=10)
        pygame.draw.rect(screen, (235, 172, 162), color_section, 4, border_radius=10)

        label_color = font.render("Choisir la couleur du pion", True, (255, 255, 255))
        screen.blit(label_color, (width // 2 - label_color.get_width() // 2, 100))

        colors = [("Rouge", (255, 0, 0)), ("Vert", (0, 255, 0)), ("Jaune", (255, 255, 0)), ("Bleu", (0, 0, 255))]
        color_buttons = []
        for idx, (name, color) in enumerate(colors):
            rect = pygame.Rect(60 + idx * 85, 140, 60, 60)
            pygame.draw.rect(screen, color, rect, border_radius=30)
            if selected_color == name:
                pygame.draw.circle(screen, (255, 255, 255), rect.center, 10)
            color_buttons.append((rect, name))

        # === Section joueurs ===
        player_section = pygame.Rect(30, 290, width - 60, 130)
        pygame.draw.rect(screen, (74, 145, 158), player_section, border_radius=10)
        pygame.draw.rect(screen, (235, 172, 162), player_section, 4, border_radius=10)

        label_player = font.render("Nombre de joueurs", True, (255, 255, 255))
        screen.blit(label_player, (width // 2 - label_player.get_width() // 2, 310))

        player_buttons = [(pygame.Rect(120, 360, 60, 40), 2), (pygame.Rect(240, 360, 60, 40), 4)]
        for rect, num in player_buttons:
            pygame.draw.rect(screen, (100, 100, 100), rect, border_radius=8)
            label = small_font.render(f"{num}", True, (255, 255, 255))
            screen.blit(label, (rect.x + 20, rect.y + 10))
            if selected_players == num:
                pygame.draw.circle(screen, (255, 255, 255), (rect.x + rect.width - 10, rect.y + 10), 8)

        # === Bouton suivant ===
        next_button = pygame.Rect(width // 2 - 60, 450, 120, 50)
        pygame.draw.rect(screen, (74, 145, 158), next_button, border_radius=10)
        pygame.draw.rect(screen, (235, 172, 162), next_button, 3, border_radius=10)
        next_label = font.render("Suivant", True, (255, 255, 255))
        screen.blit(next_label, (next_button.x + 10, next_button.y + 10))

        # === Bouton retour ===
        back_rect = pygame.Rect(20, height - 60, 50, 40)
        pygame.draw.rect(screen, (0, 0, 0), back_rect, border_radius=8)
        pygame.draw.rect(screen, (235, 172, 162), back_rect, 2, border_radius=8)
        pygame.draw.polygon(screen, (255, 255, 255), [
            (back_rect.x + 30, back_rect.y + 10),
            (back_rect.x + 20, back_rect.y + 20),
            (back_rect.x + 30, back_rect.y + 30)
        ])

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_button.collidepoint(event.pos):
                    if selected_color and selected_players:
                        print(f"Couleur choisie : {selected_color}, Nombre de joueurs : {selected_players}")
                        running = False  # Aller à l'étape suivante

                if back_rect.collidepoint(event.pos):
                    return  # Retour à l'étape précédente

                for rect, name in color_buttons:
                    if rect.collidepoint(event.pos):
                        selected_color = name

                for rect, num in player_buttons:
                    if rect.collidepoint(event.pos):
                        selected_players = num

# Test local
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((420, 700))  # Adapter à ton format
    show_classic_mode_settings(screen)
    pygame.quit()
