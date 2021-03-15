import pygame
import math
import json

from game import Game
from player import Player
from comet import Comet


pygame.init()
# définir les musiques


# définir une clock
clock = pygame.time.Clock()
FPS = 60

# génère la fenêtre du jeu
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080,720))

# charge le jeu
game = Game()

# charge l'arrière plan de notre jeu
with open("background.json", "r") as f:
    backgrounds = json.load(f)


# import charger notre bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)


# charge le bouton
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

running = True
level = None

while running:

    if game.background_change // 2 != level:
        level = game.background_change // 2
        file_name = f"assets/background/{backgrounds[str(level)]}"
        background = pygame.transform.scale(pygame.image.load(file_name), (1080, 720))

    # applique l'arrière plan
    screen.blit(background, (0, 0))

    # verifier si le jeu a commencé
    if game.is_playing:
        # déclenche les instructions de la partie
        game.update(screen)
    else:
        # ajoute l'écran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # met à jour l'affichage
    pygame.display.flip()

    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # détecte si un joueur lâche une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # détecte si la touche espace est pressée pour le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # vérification si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # met le jeu en mode lancé
                game.start()

                game.sound_manager.play('click')





    # fixer le nombre de FPS
    clock.tick(FPS)

