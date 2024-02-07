import pygame
class Player:
    def __init__(self, maze, x, y, sprite, flavour):
        self.x = x
        self.y = y
        self.sprite = sprite
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

    def setStatus(self, tile):
        pass

    def getFlavour(self):
        return self.flavour
    