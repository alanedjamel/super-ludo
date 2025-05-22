import pygame
import sys

def show_mode_selection(screen):
    pygame.font.init()
    font = pygame.font.SysFont("comicsansms", 26, bold=True)
    small_font = pygame.font.SysFont("comicsansms", 20)

    selected_mode = None
    running = True

    width, height = screen.get_size()

    # Couleurs
    BG_COLOR = (0, 0, 0)
    BOX_COLOR = (74, 145, 158)      # #4A919E
    BOX_BORDER = (235, 172, 162)    # #EBACA2
    BUTTON_COLOR = (50, 100, 200)
    BUTTON_DISABLED = (80, 80, 80)
    WHITE = (255, 255, 255)

    while running:
        screen.fill(BG_COLOR)

        # === Dimensions centrales ===
        box_width, box_height = 400, 260
        box_x = (width - box_width) // 2
        box_y = (height - box_height) // 2 - 40

        # === Section principale ===
        box_rect = pygame.Rect(box_x, box_y, box_width, box_height)
        pygame.draw.rect(screen, BOX_COLOR, box_rect, border_radius=15)
        pygame.draw.rect(screen, BOX_BORDER, box_rect, 4, border_radius=15)

        # Titre
        title = font.render("Sélectionnez le mode de jeu", True, WHITE)
        screen.blit(title, (width // 2 - title.get_width() // 2, box_y + 20))

        # --- Boutons avec cercles ---
        classic_rect = pygame.Rect(box_x + 60, box_y + 80, 220, 50)
        chrono_rect = pygame.Rect(box_x + 60, box_y + 150, 220, 50)

        pygame.draw.rect(screen, BUTTON_COLOR, classic_rect, border_radius=10)
        pygame.draw.rect(screen, BUTTON_COLOR, chrono_rect, border_radius=10)

        # Cercles
        classic_circle_pos = (classic_rect.left - 25, classic_rect.centery)
        chrono_circle_pos = (chrono_rect.left - 25, chrono_rect.centery)

        pygame.draw.circle(screen, WHITE, classic_circle_pos, 12, 2)
        pygame.draw.circle(screen, WHITE, chrono_circle_pos, 12, 2)

        # Remplir si sélectionné
        if selected_mode == "classic":
            pygame.draw.circle(screen, WHITE, classic_circle_pos, 6)
        elif selected_mode == "chrono":
            pygame.draw.circle(screen, WHITE, chrono_circle_pos, 6)

        # Textes des boutons
        classic_text = small_font.render("Mode Classique", True, WHITE)
        chrono_text = small_font.render("Mode Chrono", True, WHITE)
        screen.blit(classic_text, (classic_rect.x + 20, classic_rect.y + 12))
        screen.blit(chrono_text, (chrono_rect.x + 20, chrono_rect.y + 12))

        # === Section bouton Suivant (juste en dessous du rectangle) ===
        next_rect = pygame.Rect(width // 2 - 100, box_rect.bottom + 20, 200, 50)
        next_color = BUTTON_COLOR if selected_mode else BUTTON_DISABLED
        pygame.draw.rect(screen, next_color, next_rect, border_radius=10)
        pygame.draw.rect(screen, BOX_BORDER, next_rect, 2, border_radius=10)
        next_text = small_font.render("Suivant", True, WHITE)
        screen.blit(next_text, (next_rect.centerx - next_text.get_width() // 2, next_rect.y + 15))

        # === Bouton retour lumineux ===
        back_rect = pygame.Rect(20, height - 60, 50, 40)
        pygame.draw.rect(screen, BG_COLOR, back_rect, border_radius=10)
        pygame.draw.rect(screen, BOX_BORDER, back_rect, 2, border_radius=10)
        # Flèche
        pygame.draw.polygon(screen, WHITE, [
            (back_rect.x + 30, back_rect.y + 10),
            (back_rect.x + 20, back_rect.y + 20),
            (back_rect.x + 30, back_rect.y + 30)
        ])

        pygame.display.flip()

        # === Gestion des événements ===
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos

                if classic_rect.collidepoint((mx, my)) or (pygame.Rect(classic_circle_pos[0] - 12, classic_circle_pos[1] - 12, 24, 24).collidepoint((mx, my))):
                    selected_mode = "classic"
                elif chrono_rect.collidepoint((mx, my)) or (pygame.Rect(chrono_circle_pos[0] - 12, chrono_circle_pos[1] - 12, 24, 24).collidepoint((mx, my))):
                    selected_mode = "chrono"

                elif next_rect.collidepoint((mx, my)) and selected_mode:
                    print(f"Mode sélectionné : {selected_mode}")
                    # Appeler ici l'écran suivant selon le mode

                elif back_rect.collidepoint((mx, my)):
                    return  # Retour à l’écran précédent
