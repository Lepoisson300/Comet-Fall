import pygame
import math

from game import Game

pygame.init()

BLUE = (40, 120, 230)
GREEN = (40, 230, 120)
center_x, center_y = 320, 240
clock = pygame.time.Clock()
FPS = 60

# génère la fenêtre du jeu
pygame.display.set_caption("Comet Fall")
screen = pygame.display.set_mode((1080, 720))
# charge le jeu
game = Game()

# charge notre bannière
banner = pygame.image.load('cometfall/assets/banner.png')
banner = pygame.transform.scale(banner, (400, 400))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3.33)
banner_rect.y = 50


# charge le bouton pour lancer le jeu
play_button = pygame.image.load('cometfall/assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 300))
play_button_rect = play_button.get_rect()
play_button_rect.x = 350
play_button_rect.y = 310

# charge le bouton pour quitter le jeu
quit_button = pygame.image.load('cometfall/assets/quit_button.png')
quit_button = pygame.transform.scale(quit_button, (100, 100))
quit_button_rect = quit_button.get_rect()
quit_button_rect.x = math.ceil(screen.get_width() / 5)
quit_button_rect.y = 400

# creer le input
font = pygame.font.SysFont('Comic Sans MS,Arial', 24)
prompt = font.render('Entrez votre pseudo : ', True, BLUE)
prompt_rect = prompt.get_rect(center=(center_x, center_y))

# faire un input pour rentrer son pseudo
user_input_value = ""
user_input = font.render(user_input_value, True, GREEN)
user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)

pseudo_input = True
while pseudo_input:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pseudo_input = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                pseudo_input = False
                break
            elif event.key == pygame.K_BACKSPACE:
                user_input_value = user_input_value[:-1]
            else:
                user_input_value += event.unicode
            user_input = font.render(user_input_value, True, GREEN)
            user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)

    clock.tick(30)
    screen.fill(0)  # set background color to black
    screen.blit(prompt, prompt_rect)
    screen.blit(user_input, user_input_rect)
    pygame.display.flip()

# main menu
running = True

while running:
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

    # met à jour l'affichage
    pygame.display.flip()

    for event in pygame.event.get():
        # détecte si un joueur lâche une touche du clavier
        if event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # détecte si la touche espace est pressée pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
                # génere l'image de mon joueur en mode tir
                player_T = pygame.image.load('cometfall/assets/player_T.png')
                screen.blit(player_T, game.player.rect)

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # vérification si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                if not game.is_playing:
                    game.start()

            elif quit_button_rect.collidepoint(event.pos):
                running = False
                pygame.quit()

        elif event.type == pygame.QUIT:
            running = False
            pygame.quit()

    # fixer le nombre de FPS
    clock.tick(FPS)

