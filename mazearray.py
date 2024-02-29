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
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] == "#":
                    self.setTile(x, y, self.chooseTile("filling"))
        self.grid = [x + [[0]] for x in self.grid] 
        #force 0 to generate as an array. this is because all the other numbers generate as lists. 
        #the reason for this is unknown however it doesn't affect much so i'd rather not spend 10 hours fixing this behaviour i only have about a month to get this done

    def setTile(self, x, y, input):
        self.grid[y][x] = input

    def getTile(self, x, y):
        return self.grid[y][x]

    def chooseTile(self, mode):
        if mode == "safe":
            return random.choices(range(1,6))
            #return[1]
        elif mode == "filling":
            return random.choices(range(1,8), weights=(0.1, 0.1, 0.1, 0.1, 0.15, 0.2, 0.2))
            #return ["#"]
        else:
            return random.choices([1, 3, 4, 5])
        #red/yellow is 3x more likely with "unsafe" generation, this is because red/yellow tiles are not generated during path generation.

    def generatePath(self):
        random.seed(self.seed)
        lastTile = 0 #need to keep track of last tile. 
        stillOrange = False
        #If a purple was placed, direction must be the same for one tile. If an orange tile was placed, do not use blue until purple is placed.
        #start halfway down the maze, at x = 0, because it is player spawn point
        y = round(((self.height)/2))
        x = 0
        chosenTile = None
        while x != (self.width):
            self.setTile(x, y, chosenTile)
            self.solpath.append([x, y, chosenTile])
            if lastTile == [4] or stillOrange:
                stillOrange = True
                chosenTile = self.chooseTile("")
                if chosenTile == [5]:
                    stillOrange = False
            else:
                chosenTile = self.chooseTile("safe") #pick a new tile
            if not lastTile == [5]: #only change axis when purple tile not changed
                axis = random.choice(["x", "x", "y"])
            elif lastTile == [2]:
                for i in (-1, 1):
                    self.setTile(x + i, y, self.chooseTile("safe"))
                    self.setTile(x, y + i, self.chooseTile("safe"))
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
            lastTile = chosenTile

        #place a pink tile at player spawn, AFTER path generation
        self.setTile(0, round(((self.height)/2)), [1])


if __name__ == "__main__": #used for testing
    maze = MazeArray(4,4,255) 
    maze.generatePath()
    maze.fillMaze()
    for row in maze.grid:
        print(*row, sep="\t")
    #print(maze.getTile(0,0))
    print(maze.solpath)