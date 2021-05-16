import pygame


class AnimateSprite(pygame.sprite.Sprite):

    # définir les choses a faire a la créations de l'entité
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        image = pygame.image.load(f'cometfall/assets/{sprite_name}.png')
        self.image = pygame.transform.scale(image, size)
        self.current_image = 0  # commencer l'animation a l'image 0
        self._images = animation.get(sprite_name)
        self.im_index = 0
        self.animation = False

    def set_images(self, name):
        self._images = animation.get(name)

    # définir une methode pour démarer l'animation
    def start_animation(self):
        self.animation = True

    #  définir une methode pour animer le sprite
    def animate(self, loop=False):
        self.im_index = (self.im_index + 1) % len(self._images)
        self.image = pygame.transform.scale(self._images[self.im_index], self.size)
        # If we have used all images
        if not loop and self.im_index == 0:
            self.animation = False


# définir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name, number_of_images, *, slow_factor=1):
    # charger les 24 images de ce sprite correspondant
    images = []
    path = f"cometfall/assets/{sprite_name}/{sprite_name}"

    for num in range(1, number_of_images+1):
        image_path = path + f'{num}.png'
        print(image_path)
        images.extend([pygame.image.load(image_path)] * slow_factor)

    return images


# definir un dictionnaire qui va contenir les images chargées de chaque sprite
# mummy -- [...mummy1.png, ...mummy2.png, ...]
animation = {
    'mummy': load_animation_images('mummy', 24),
    'player': load_animation_images('player', 8, slow_factor=3),
    'player_left': load_animation_images('player_left', 8, slow_factor=3),
    'alien': load_animation_images('alien', 24),
    'squeletton': load_animation_images('squeletton', 6, slow_factor=5),
    'dragon': load_animation_images('dragon', 10, slow_factor=3),
    'tree': load_animation_images('tree', 4, slow_factor=10),
    'rock': load_animation_images('rock', 9, slow_factor=8),
}
