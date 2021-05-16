import json

import pygame
import numpy as np

from comet import CometFallEvent
from player import Player
import monster
from sounds import SoundManager
from database import basedonnee



class Game:

    MAX_LEVEL = 3
    LEVEL_INCREMENT = 1

    def __init__(self):
        self.is_playing = False
        self.player = Player(self)
        self.all_players = pygame.sprite.Group([self.player])
        self.comet_event = CometFallEvent(self)
        self.all_monster = pygame.sprite.Group()
        self.sound_manager = SoundManager()
        self.font = pygame.font.Font("cometfall/assets/fonts/Anton-Regular.ttf", 30)
        self.score = 0
        self.level = {}
        self.username = None
        self.comet_event_number = 0
        image = pygame.image.load(f"cometfall/assets/background/planet.jpg")
        self.background = pygame.transform.scale(image, (1200, 720))

    @property
    def key_pressed(self):
        return pygame.key.get_pressed()

    def start(self):
        self.is_playing = True
        self.load_level()
        self.spawn_monsters()
        self.sound_manager.play('click')

    def spawn_monsters(self, n=None):
        """ Spawn n monsters with probability for each monster to appear """
        monsters_type = self.level['monsters']
        probability = self.level.get('probability')
        attack_factor = 1 + int(self.level.get('attack_bonus', '0%')[:-1]) / 100
        health_factor = 1 + int(self.level.get('health_bonus', '0%')[:-1]) / 100
        player_factor = 1 + int(self.level.get('player_bonus', '0%')[:-1]) / 100
        self.player.attack *= player_factor
        spawn_number = n or int(self.level.get('spawn_number'))
        monsters = np.random.choice(monsters_type, spawn_number, p=probability)

        for name in monsters:
            try:
                monster_type = getattr(monster, name.title())
            except AttributeError:
                raise AttributeError(
                    f"Monster {name.title()} not exists, check the levels.json file")
            self.all_monster.add(monster_type(self, health_factor, attack_factor))

    def add_score(self, points=10):
        self.score += points

    @staticmethod
    def check_colision(sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False,
                                           pygame.sprite.collide_mask)

    def game_over(self):
        """ Remet le jeu à neuf """
        self.all_monster = pygame.sprite.Group()
        self.comet_event.all_comet = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        self.player.rect.x = 400
        self.player.rect.y = 470
        self.load_level(1)
        self.sound_manager.stop_all()
        self.sound_manager.play('game_over')
        print()
        a = basedonnee()
        a.enregistrer()
        a.score()



    def update(self, screen):
        """ Update the screen display"""
        score_text = self.font.render(f"Score : {self.score}", True, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        username = self.font.render(self.username, True, (0, 0, 0))
        screen.blit(username, (950, 20))

        # appliquer l'image du joueur
        if self.key_pressed[pygame.K_LCTRL]:  # shoot mode
            screen.blit(self.player.shoot_image, self.player.rect)
        elif self.player.animation:
            self.player.animate()
            screen.blit(self.player.image, self.player.rect)
        else:
            screen.blit(self.player.default_image, self.player.rect)
        self.player.update_health_bar(screen)
        self.comet_event.update_bar(screen)

        # récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # récupérer les monstres de notre jeu
        for active_monster in self.all_monster:
            active_monster.forward()
            active_monster.update_health_bar(screen)
            active_monster.update_animation()

        # récupérer les comètes de notre jeu
        for comet in self.comet_event.all_comet:
            comet.fall()

        # récuperer le boss de notre jeu
        """
        for Boss in self.Boss_event.ship:
            Boss.fall()
        """
        self.player.all_projectiles.draw(screen)
        self.comet_event.all_comet.draw(screen)
        self.all_monster.draw(screen)

        # verifier si le joueur souhaite aller à gauche ou à droite
        if not self.key_pressed[pygame.K_LCTRL]:
            if self.key_pressed[pygame.K_RIGHT] and \
                    self.player.rect.x + self.player.rect.width < screen.get_width():
                self.player.move_right()
            elif self.key_pressed[pygame.K_LEFT] and self.player.rect.x > 0:
                self.player.move_left()

    def load_level(self, wanted_level=None):
        """
        Apply values defined in levels.json for current level
        """
        if self.comet_event_number % self.LEVEL_INCREMENT == 0:
            level = wanted_level or (self.comet_event_number // self.LEVEL_INCREMENT + 1)
            if level <= self.MAX_LEVEL:
                with open("cometfall/static/levels.json", 'r', encoding='utf-8') as f:
                    self.level = json.load(f)[f"level {level}"]

                image = pygame.image.load(
                    f"cometfall/assets/background/{self.level['background']}")
                self.background = pygame.transform.scale(image, (1080, 720))
                if sound := self.level.get('game_sound'):
                    self.sound_manager.stop_all()
                    self.sound_manager.play(sound, volume=0.15)
                else:
                    raise AttributeError(f"You must define a game_sound attribute "
                                         f"for the level {level}")
