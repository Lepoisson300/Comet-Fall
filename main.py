import pygame
import math
from game import  Game
from player import  Player
pygame.init()

# générer la fenetre de ntre jeu
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080,720))

#charger notre jeu
game = Game()

# importer charger  l'arriere plan de notre jeu
background = pygame.image.load('assets/bg.jpg')

# import charger notre banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)


#import charger notre bouton
play_button =  pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

running = True

# boucle tant que cette condition est vraie
while running:

    # appliquer l'arriere plan
    screen.blit(background, (0, -200))

    # verifier si le jeu a commencé
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)
    else:
        # ajouetr mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)



    #mettre a jour notre ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
    # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # detectecter si un joueur lache une touche du clavier
        elif  event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est pressé pour notre projectile
            if event.key == pygame.K_SPACE:
                game.player.lunch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifictaion si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode lancé
                game.start()

