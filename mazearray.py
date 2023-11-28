import random      
class MazeArray:

    def __init__(self, width, height, seed):
        self.width = width
        self.height = height
        self.seed = seed
        self.grid = [[0 for x in range(self.width)] for y in range(self.height)]

        self.tile_id = {
            "GOAL": 0, #tile used to mark end of maze, do not generate
            "PINK": 1,
            "BLUE": 2,
            "GREEN": 3,
            "ORANGE": 4,
            "PURPLE": 5,
            "RED": 6,
            "YELLOW": 7,
            "BLUE_ELEC": 8 #blue tiles next to yellow tiles will be converted to this tile, do not generate
        }

    def generateMaze(self):
        pass
    def generatePath(self):
        random.seed = self.seed
        #start halfway down the maze, at x = 0. This is also where the player spawns
        y = round(((self.height)/2))
        x = 0
        while x != self.width:
            self.grid[x][y] = random.randint(1,5)
            #decide whether to change x or y
            #pick a direction (+1 or -1)
            #check if that tile is occupied (grid[x][y] != 0)
            #if occupied, multiply direction by -1
            
            pass   