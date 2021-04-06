import sys

import pygame
from game import Game


BLUE = (40, 120, 230)
GREEN = (40, 230, 120)


def ask_username_input():
    font = pygame.font.SysFont('Comic Sans MS,Arial', 24)
    prompt = font.render('Entrez votre pseudo : ', True, BLUE)
    prompt_rect = prompt.get_rect(topleft=(300, 250))

    # Ask user's nickname
    username = ""
    user_input = font.render(username, True, GREEN)
    user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)

    def check_input(screen):
        nonlocal username, user_input

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                    return username
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode
                user_input = font.render(username, True, GREEN)

            screen.fill(0)  # set background color to black
            screen.blit(prompt, prompt_rect)
            screen.blit(user_input, user_input_rect)

    return check_input


def commands(game,screen):
    font = pygame.font.SysFont('Comic Sans MS,Arial', 34)
    text_1 = font.render('Here is the commands of the game !', True, BLUE)
    text_1_rect = text_1.get_rect(topleft=(250, 150))

    # afficher la première commande
    comand1 = pygame.image.load("cometfall/assets/command/command1.png")

    # afficher la deuxième commande
    comand2 = pygame.image.load("cometfall/assets/command/command2.png")
    
    button = pygame.image.load("cometfall/assets/back_button.png")
    button_rect = button.get_rect(topleft=(10, 650))

    # afficher l'arriere plan
    screen.blit(game.background, (0, 0))

    # afficher la premiere command
    screen.blit(comand1, (10, 300))
    screen.blit(text_1, text_1_rect)
    screen.blit(comand2, (10, 500))
    screen.blit(button, button_rect)
    pygame.display.flip()  # met à jour l'affichage

