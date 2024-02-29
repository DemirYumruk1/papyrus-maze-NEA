import pygame
class Player:
    def __init__(self, x, y, sprite_path, sprite_width):
        self.x = x
        self.y = y
        sprite = pygame.image.load(sprite_path)
        self.sprite_width = sprite_width # only need width, sprite should be 1:1
        self.sprite = pygame.transform.scale(sprite, (sprite_width, sprite_width))
        self.flavour = False

    def move(self, direction_y, direction_x, max_y, max_x):
        #Constrain movement
        if (self.y >= max_y):
            if direction_y == 1:
                return            
        elif self.y == 0:
            if direction_y == -1:
                return
        if (self.x >= max_x):
            if direction_x == 1:
                return
        elif self.x == 0:
            if direction_x == -1:
                return
        
        self.y += direction_y
        self.x += direction_x

    #note to self, flavour is a boolean to save memory (a string/int/float would take more memory)
    #this also helps with the if statement for checking water collision when orange flavour is on
    #orange = True, lemon = False.
    def setFlavour(self, flavour):
        self.flavour = flavour

    def getFlavour(self):
        return self.flavour
    
    def getXpos(self):
        return int(self.x)
    
    def getYpos(self):
        return int(self.y)
    
    def getXY(self):
        return[self.x][self.y]

    def setSprite(self, sprite_path):
        sprite = pygame.image.load(sprite_path)
        self.sprite = pygame.transform.scale(sprite, (self.sprite_width, self.sprite_width))


    