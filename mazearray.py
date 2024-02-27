import random      
class MazeArray:

    def __init__(self, width, height, seed):
        self.width = width
        self.height = height
        self.seed = seed
        self.grid = [["#" for x in range(self.width)] for y in range(self.height)]
        self.solpath = []

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getGrid(self):
        return self.grid

    def fillMaze(self):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[y][x] == "#":
                    self.setTile(x, y, self.chooseTile(False))
        self.grid = [x + [[0]] for x in self.grid] 
        #force 0 to generate as an array. this is because all the other numbers generate as lists. 
        #the reason for this is unknown however it doesn't affect much so i'd rather not spend 10 hours fixing this behaviour i only have about a month to get this done

    def setTile(self, x, y, input):
        self.grid[y][x] = input

    def getTile(self, x, y):
        print(self.grid[y][x])
        return self.grid[y][x]

    def chooseTile(self, safe):
        if safe:
            return random.choices(range(1,6))
        else:
            #return random.choices(range(1,8), weights=(0.1, 0.1, 0.15, 0.15, 0.15, 0.2, 0.2))
            return [6] 
        #red/yellow is 3x more likely with "unsafe" generation, this is because red/yellow tiles are not generated during path generation.

    def generatePath(self):
        random.seed = self.seed
        lastTile = 0 #need to keep track of last tile. 
        #If a purple was placed, direction must be the same for one tile. If an orange tile was placed, do not use blue until purple is placed.
        #start halfway down the maze, at x = 0, because it is player spawn point
        y = round(((self.height)/2))
        x = 0
        #print(x)
        #print(y)
        while x != (self.width): #+1 removed, thought it would end loop after filling, caused overflow, reverted
            chosenTile = self.chooseTile(True) #pick a new tile
            direction = 0
            #print(x)
            #print(y)
            self.setTile(x, y, chosenTile)
            self.solpath.append([x, y, chosenTile])
            axis = random.choice(["x", "x", "y"])   #2/3 chance of changing x
            #print(axis)
            if axis == "x":
                direction = random.choice([-1, -1, 1, 1, 1])    #weighting the algorithm to the right to be less prone to walking into itself
                if x == 0:
                    direction = 1
                if self.grid[y][x] != 0:
                    x += direction
                else:
                    direction *= -1
                    x += direction
                #print(x)
            if axis == "y":
                direction = random.choice([-1, 1])
                if y == self.height -1:
                    direction = -1
                if y == 0:
                    direction = 1
                y += direction
                #print(y)


        #place a pink tile at player spawn, AFTER path generation
        maze.setTile(0, round(((self.height)/2)), [1])


if __name__ == "__main__": #used for testing
    maze = MazeArray(4,4,255) 
    maze.generatePath()
    maze.fillMaze()
    for row in maze.grid:
        print(*row, sep="\t")
    print(maze.solpath)