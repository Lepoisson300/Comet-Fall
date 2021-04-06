import pygame
from game import Game

pygame.init()

BLUE = (40, 120, 230)
GREEN = (40, 230, 120)
command = False
game = Game()
background = pygame.image.load('assets/background/planet.jpg')

# génère la fenêtre du jeu
pygame.display.set_caption("Comet Fall")
screen = pygame.display.set_mode((1080, 720))


# set background color to black
while True:
    screen.blit(background, (0, 0))
