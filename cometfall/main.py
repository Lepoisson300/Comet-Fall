import sys

import pygame

from game import Game
from interface import Interface

pygame.init()

BLUE = (40, 120, 230)
GREEN = (40, 230, 120)
center_x, center_y = 320, 240
clock = pygame.time.Clock()
FPS = 60
command = False

# génère la fenêtre du jeu
pygame.display.set_caption("Comet Fall")
screen = pygame.display.set_mode((1080, 720))
game = Game()  # charge le jeu
ui = Interface(screen)

check_input = ui.ask_username_input()
while not (username := check_input()):
    pygame.display.flip()  # met à jour l'affichage
    clock.tick(FPS)
else:
    game.username = username

while True:
    screen.blit(game.background, (0, 0))
    # verifier si le jeu a commencé
    if game.is_playing:
        # déclenche les instructions de la partie
        game.update(screen)
    elif ui.commands_isshow:
        ui.show_commands()
    else:
        ui.main_menu()

    for event in pygame.event.get():
        # détecte si un joueur lâche une touche du clavier
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.key_pressed[pygame.K_LCTRL]:
                game.player.launch_projectile()

        elif not game.is_playing and event.type == pygame.MOUSEBUTTONDOWN:
            # vérification si la souris est en collision avec le bouton jouer
            if ui.play_button_rect.collidepoint(event.pos):
                if not game.is_playing:
                    game.start()

            elif not ui.commands_isshow and ui.quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit(0)

            elif not ui.commands_isshow and \
                    ui.command_button_rect.collidepoint(event.pos):
                ui.commands_isshow = True

            elif ui.commands_isshow and ui.back_button_rect.collidepoint(event.pos):
                ui.commands_isshow = False

        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    pygame.display.flip()  # met à jour l'affichage
    clock.tick(FPS)  # fixer le nombre de FPS
