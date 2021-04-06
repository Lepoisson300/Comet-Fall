import sys

import pygame
from pygame.image import load
from pygame.transform import scale

from game import Game
import interface

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

# charge notre bannière
banner = scale(load('cometfall/assets/banner_1.png'), (400, 400))
banner_rect = banner.get_rect()
banner_rect.x, banner_rect.y = (320, 110)

# charge le bouton pour lancer le jeu
play_button = scale(load('cometfall/assets/button_1.png'), (370, 100))
play_button_rect = play_button.get_rect()
play_button_rect.x, play_button_rect.y = (360, 400)

# charge le bouton pour quitter le jeu
quit_button = pygame.transform.scale(load('cometfall/assets/quit_button.png'), (160, 60))
quit_button_rect = quit_button.get_rect()
quit_button_rect.x, quit_button_rect.y = 10, 650

# charge le bouton pour les commandes
command_button = pygame.transform.scale(load('cometfall/assets/command_buton.png'), (160, 60))
command_button_rect = command_button.get_rect()
command_button_rect.x, command_button_rect.y = 910, 650

check_input = interface.ask_username_input()
while not (username := check_input(screen)):
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
    else:
        # ajoute l'écran de bienvenue
        screen.blit(quit_button, quit_button_rect)
        screen.blit(command_button, command_button_rect)
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)

    for event in pygame.event.get():
        # détecte si un joueur lâche une touche du clavier
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.key_pressed[pygame.K_LCTRL]:
                game.player.launch_projectile()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # vérification si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                if not game.is_playing:
                    game.start()

            elif quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit(0)

            elif command_button_rect.collidepoint(event.pos):
                interface.commands(game, screen)
                while True:
                    pygame.display.flip()  # met à jour l'affichage
                    clock.tick(FPS)

        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    pygame.display.flip()  # met à jour l'affichage
    clock.tick(FPS)  # fixer le nombre de FPS
