import pygame

class SoundManager:

    def __init__(self):
        self.sounds ={
            'click': pygame.mixer.Sound("assets/sounds/click.ogg"),
            'game_over': pygame.mixer.Sound("assets/sounds/game_over.ogg"),
            'meteorite': pygame.mixer.Sound("assets/sounds/meteorite.ogg"),
            'tir': pygame.mixer.Sound("assets/sounds/tir.ogg"),
            'protect-2x': pygame.mixer.Sound("assets/sounds/protect-2x.mp3")
        }

    def play(self, name):
        self.sounds[name].play()