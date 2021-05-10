import sys

import pygame
from pygame.image import load
from pygame.transform import scale


class Interface:
    BLUE = (40, 120, 230)
    GREEN = (40, 230, 120)

    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Comic Sans MS,Arial', 24)

        # charge le bouton pour lancer le jeu
        self.play_button = scale(load('cometfall/assets/button_1.png'), (370, 100))
        self.play_button_rect = self.play_button .get_rect()
        self.play_button_rect.x, self.play_button_rect.y = (360, 400)
        # charge le bouton pour quitter le jeu
        self.quit_button = scale(load('cometfall/assets/quit_button.png'), (160, 60))
        self.quit_button_rect = self.quit_button.get_rect()
        self.quit_button_rect.x, self.quit_button_rect.y = 10, 650
        # charge le bouton pour les commandes
        self.command_button = scale(load('cometfall/assets/command_buton.png'), (160, 60))
        self.command_button_rect = self.command_button.get_rect()
        self.command_button_rect.x, self.command_button_rect.y = 910, 650

        # return button in commands interface
        self.back_button = pygame.image.load("cometfall/assets/back_button.png")
        self.back_button_rect = self.back_button.get_rect(topleft=(10, 650))
        self.commands_isshow = False

    def ask_username_input(self):
        prompt = self.font.render('Entrez votre pseudo : ', True, self.BLUE)
        prompt_rect = prompt.get_rect(topleft=(300, 250))

        # Ask user's nickname
        username = ""
        user_input = self.font.render(username, True, self.GREEN)
        user_input_rect = user_input.get_rect(topleft=prompt_rect.topright)

        def check_input():
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
                    user_input = self.font.render(username, True, self.GREEN)

                self.screen.fill(0)  # set background color to black
                self.screen.blit(prompt, prompt_rect)
                self.screen.blit(user_input, user_input_rect)

        return check_input

    def show_commands(self):
        text_1 = self.font.render('Here is the commands of the game !', True, self.BLUE)
        text_1_rect = text_1.get_rect(topleft=(250, 150))
        command1 = pygame.image.load("cometfall/assets/command/command1.png")
        command2 = pygame.image.load("cometfall/assets/command/command2.png")
        self.commands_isshow = True

        self.screen.blit(command1, (10, 300))
        self.screen.blit(text_1, text_1_rect)
        self.screen.blit(command2, (10, 500))
        self.screen.blit(self.back_button, self.back_button_rect)

    def main_menu(self):
        # charge notre bannière
        banner = scale(load('cometfall/assets/banner_1.png'), (400, 400))
        banner_rect = banner.get_rect()
        banner_rect.x, banner_rect.y = (320, 110)

        self.screen.blit(self.quit_button, self.quit_button_rect)
        self.screen.blit(self.command_button, self.command_button_rect)
        self.screen.blit(banner, banner_rect)
        self.screen.blit(self.play_button, self.play_button_rect)
