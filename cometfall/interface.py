import sys

import pygame

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
