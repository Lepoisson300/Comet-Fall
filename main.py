import pygame
import math
import json

from game import Game
from player import Player
from comet import Comet


pygame.init()

BLUE = (40, 120, 230)
GREEN = (40, 230, 120)

center_x, center_y = 320, 240

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


# charge le bouton pour lancer le jeu
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charge le bouton pour quitter le jeu
quit_button = pygame.image.load('assets/quit_button.png')
quit_button = pygame.transform.scale(quit_button, (100, 100))
quit_button_rect = quit_button.get_rect()
quit_button_rect.x = math.ceil(screen.get_width() / 5)
quit_button_rect.y = math.ceil(screen.get_height() / 2)

running = True
level = None

# creer le input
font = pygame.font.SysFont('Comic Sans MS,Arial', 24)
prompt = font.render('Entrez votre pseudo : ', True, BLUE)
prompt_rect = prompt.get_rect(center=(center_x, center_y))


# faire un input pour rentrer son pseudo
user_input_value = ""
user_input = font.render(user_input_value, True, GREEN)
user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                continuer = False
                break
            elif event.key == pygame.K_BACKSPACE:
                user_input_value = user_input_value[:-1]
            else:
                user_input_value += event.unicode
            user_input = font.render(user_input_value, True, GREEN)
            user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)

    clock.tick(30)

    screen.fill(0)
    screen.blit(prompt, prompt_rect)
    screen.blit(user_input, user_input_rect)
    pygame.display.flip()

while running:

    if game.background_change // 2 != level:
        level = game.background_change // 3
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
        screen.blit(quit_button, quit_button_rect)
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

            # détecte si la touche espace est pressée pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # vérification si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # met le jeu en mode lancé
                game.start()
                menu_sound = pygame.mixer.Sound('assets/sounds/protect-2x.mp3')
                menu_sound.set_volume(0.2)
                menu_sound.play()
                game.sound_manager.play('click')

            elif quit_button_rect.collidepoint(event.pos):
                pygame.quit()

    # fixer le nombre de FPS
    clock.tick(FPS)

