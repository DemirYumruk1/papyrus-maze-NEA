import pygame
from mazearray import MazeArray
class Game:
    def __init__(self, maze_width, maze_height, seed):
        self.seed = seed
        self.maze = MazeArray(maze_width, maze_height, seed)
        self.maze_width = maze_width
        self.maze_height = maze_height
        self.mazeArray = self.maze.getGrid()
        self.tile_id = {
            0: "GOAL", #tile used to mark end of maze, do not generate
            1: "PINK",
            2: "BLUE",
            3: "GREEN",
            4: "ORANGE",
            5: "PURPLE",
            6: "RED",
            7: "YELLOW",
            8: "BLUE_ELEC" #blue tiles next to yellow tiles will be converted to this tile, do not generate
        }
        #tiles are 16x16 so the window must be 16 times the amount of tiles to display them all
        self.window_width = maze_width * 16
        self.window_height = maze_height * 16

        self.tile_width = 16 #only need width, the tiles are square

        #game window size must be based on tiles
        self.game_window = pygame.display.set_mode((self.window_width,self.window_height))

    def draw(self):
        self.game_window.fill(0)
        for j, row in enumerate(self.mazeArray):
            for i, tile in enumerate(row):
                colour = self.tile_id[tile[0]] #tile[0], because the tile itself contains a list ([1] instead of 1)
                pygame.draw.rect(self.game_window, colour, (i * self.tile_width, j * self.tile_width, self.tile_width, self.tile_width))
                #print(self.mazeArray[i][j])
                #if self.mazeArray[i][j] == 1:
                #    pygame.draw.rect(self.game_window, "pink", (i * 16, j * 16), (16, 16))
                #elif self.mazeArray[i][j] == 2:
                #    pygame.draw.rect(self.game_window, "blue", (i * 16, j * 16), (16, 16))
                #elif self.mazeArray[i][j] == 8:
                #    pygame.draw.rect(self.game_window, "blue", (i * 16, j * 16), (16, 16))
                #elif self.mazeArray[i][j] == 3:
                #    pygame.draw.rect(self.game_window, "green", (i * 16, j * 16), (16, 16))
                #elif self.mazeArray[i][j] == 4:
                #    pygame.draw.rect(self.game_window, "orange", (i * 16, j * 16), (16, 16))
                #elif self.mazeArray[i][j] == 5:
                #    pygame.draw.rect(self.game_window, "purple", (i * 16, j * 16), (16, 16))
                #elif self.mazeArray[i][j] == 6:
                #    pygame.draw.rect(self.game_window, "red", (i * 16, j * 16), (16, 16))
                #elif self.mazeArray[i][j] == 7:
                #    pygame.draw.rect(self.game_window, "yellow", (i * 16, j * 16), (16, 16))
        
        pygame.display.update()

    def run_game_loop(self):
        #initialise game
        pygame.init()
        self.maze.generatePath()
        self.maze.fillMaze()
        #main loop
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
            self.draw()

if __name__ == "__main__":
    game = Game(10,10,255)
    game.run_game_loop()