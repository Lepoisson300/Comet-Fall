import pygame


class SoundManager:

    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound("cometfall/assets/sounds/click.ogg"),
            'game_over': pygame.mixer.Sound("cometfall/assets/sounds/game_over.ogg"),
            'meteorite': pygame.mixer.Sound("cometfall/assets/sounds/meteorite.ogg"),
            'tir': pygame.mixer.Sound("cometfall/assets/sounds/tir.ogg"),
            'protect-2x': pygame.mixer.Sound("cometfall/assets/sounds/protect-2x.mp3")
        }

    def play(self, name, volume=1):
        self.sounds[name].set_volume(volume)
        self.sounds[name].play()

    def stop(self, name):
        self.sounds[name].stop()

    def stop_all(self):
        for sound in self.sounds.values():
            sound.stop()
