import pygame
class Player:
    def __init__(self, x, y, sprite_path, sprite_width, flavour):
        self.x = x
        self.y = y
        sprite = pygame.image.load(sprite_path)
        self.sprite_width = sprite_width # only need width, sprite should be 1:1
        self.sprite = pygame.transform.scale(sprite, (sprite_width, sprite_width))
        self.flavour = flavour

    def move(self, direction_y, direction_x, max_y, max_x):
        #Constrain movement
        if (self.y >= max_y - self.height):
            if direction_y == 1:
                return            
        elif self.y == 0:
            if direction_y == -1:
                return
        if (self.x >= max_x - self.width):
            if direction_x == 1:
                return
        elif self.x == 0:
            if direction_x == -1:
                return

    def setFlavour(self, flavour):
        self.flavour = flavour

    def getFlavour(self):
        return self.flavour

    def setSprite(self, sprite_path):
        sprite = pygame.image.load(sprite_path)
        self.sprite = pygame.transform.scale(sprite, (self.sprite_width, self.sprite_width))


    