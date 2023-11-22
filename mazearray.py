        
class MazeArray:

    def __init__(self, width, height):
        self.width = width
        self.height = height

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
        start_y = (self.height)/2
        pass