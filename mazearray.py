import random      
class MazeArray:
#TODO: sin() function path generation.
    def __init__(self, width, height, seed):
        self.width = width
        self.height = height
        self.seed = seed
        self.grid = [["#" for x in range(self.width)] for y in range(self.height)]

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

    def fillMaze(self):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[x][y] == "#":
                    self.grid[x][y] = self.chooseTile(False)
                    #newtile = triangularly distributed number idk
                    #self.setTile(i, j, newtile)
                    pass

    def setTile(self, x, y, input):
        self.grid[x][y] = input

    def chooseTile(self, safe):
        if safe:
            return random.choices(range(1,6))
        else:
            return random.choices(range(1,8), weights=(0.1, 0.1, 0.1, 0.1, 0.1, 0.3, 0.3)) 
        #red/yellow is 3x more likely with "unsafe" generation, this is because red/yellow tiles are not generated during path generation.

    def generatePath(self):
        random.seed = self.seed
        #start halfway down the maze, at x = 0, because it is player spawn point
        y = round(((self.height)/2))
        x = 1
        #print(x)
        #print(y)
        while x != (self.width): #+1 removed, thought it would end loop after filling, caused overflow, reverted
            direction = 0
            #print(x)
            #print(y)
            self.setTile(x, y, self.chooseTile(True))
            axis = random.choice(["x", "x", "y"])   #2/3 chance of changing x
            #print(axis)
            if axis == "x":
                direction = random.choice([-1, -1, 1, 1, 1])    #weighting the algorithm to the right to be less prone to walking into itself
                if x == 0:
                    direction = 1
                if self.grid[x][y] != 0:
                    x += direction
                else:
                    direction *= -1
                    x += direction
                #print(x)
            if axis == "y":
                direction = random.choice([-1, 1])
                if y == self.height:
                    direction = -1
                if y == 0:
                    direction = 1
                y += direction
                #print(y)
            #check if that tile is occupied (grid[x][y] != 0)
            #if occupied, multiply direction by -1
            #note: algorithm seems to start from coordinates (x,0) [somewhere from the bottom]  instead of (0,y/2) [halfway down, at the first column] for reasons i cannot decipher. 
            #This algorithm only exists to generate test cases so fixing this is low-priority

if __name__ == "__main__": #used for testing
    maze = MazeArray(10,10,255) 
    maze.generatePath()
    maze.fillMaze()
    for row in maze.grid:
        print(*row, sep="\t")