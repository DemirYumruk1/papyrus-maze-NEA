import random      
class MazeArray:

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

    def generateMaze(self):
        pass
    def generatePath(self):
        random.seed = self.seed
        #start halfway down the maze, at x = 0, because it is player spawn point
        y = round(((self.height)/2))
        x = 1
        print(x)
        print(y)
        while x != (self.width + 1): #+1 is because the loop should terminate after the last tile is filled
            direction = 0
            self.grid[x][y] = random.randint(1,5)
            axis = random.choice(["x", "x", "y"])   #2/3 chance of changing x
            print(axis)
            if axis == "x":
                direction = random.choice([-1, -1, 1, 1, 1])    #weighting the algorithm to the right to be less prone to walking into itself
                if x == 0:
                    direction = 1
                if self.grid[x][y] != 0:
                    x += direction
                else:
                    direction *= -1
                    x += direction
                print(x)
            if axis == "y":
                direction = random.choice([-1, 1])
                if y == self.height:
                    direction = -1
                if y == 0:
                    direction = 1
                y += direction
                print(y)
            #check if that tile is occupied (grid[x][y] != 0)
            #if occupied, multiply direction by -1

if __name__ == "__main__":
    maze = MazeArray(10,10,100) #test case
    maze.generatePath()
    print(maze.grid)