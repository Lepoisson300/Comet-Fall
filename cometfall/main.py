import sys
import math

import pygame

from game import Game
import interface

pygame.init()

clock = pygame.time.Clock()
FPS = 60

# génère la fenêtre du jeu
pygame.display.set_caption("Comet Fall")
screen = pygame.display.set_mode((1080, 720))
game = Game()  # charge le jeu

# charge notre bannière
banner = pygame.image.load('cometfall/assets/banner_1.png')
banner = pygame.transform.scale(banner, (400, 400))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3.33)
banner_rect.y = 110

# charge le bouton pour lancer le jeu
play_button = pygame.image.load('cometfall/assets/button_1.png')
play_button = pygame.transform.scale(play_button, (370, 100))
play_button_rect = play_button.get_rect()
play_button_rect.x = 365
play_button_rect.y = 415

# charge le bouton pour quitter le jeu
quit_button = pygame.image.load('cometfall/assets/quit_button.png')
quit_button = pygame.transform.scale(quit_button, (200, 60))
quit_button_rect = quit_button.get_rect()
quit_button_rect.x = 150
quit_button_rect.y = 440

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
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)

    for event in pygame.event.get():
        # détecte si un joueur lâche une touche du clavier
        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # détecte si la touche espace est pressée pour lancer le projectile
            if event.key == pygame.KMOD_CTRL :
                game.player.launch_projectile()
            elif event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # vérification si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                if not game.is_playing:
                    game.start()

            elif quit_button_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit(0)

        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    pygame.display.flip()  # met à jour l'affichage
    clock.tick(FPS)  # fixer le nombre de FPS

