import pygame
from mazearray import MazeArray
from player import Player
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

        #the player's sprite must also be proportional to the tile size
        self.Player = Player(0, maze_height/2, "Assets/player_normal.png", self.tile_width, False)




    def draw(self):
        self.game_window.fill(0) #refresh screen
        player_displayed_pos_x = self.Player.x * self.tile_width
        player_displayed_pos_y = self.Player.y * self.tile_width
        for j, row in enumerate(self.mazeArray):
            for i, tile in enumerate(row):
                colour = self.tile_id[tile[0]] #tile[0], because the tile itself contains a list ([1] instead of 1)
                pygame.draw.rect(self.game_window, colour, (i * self.tile_width, j * self.tile_width, self.tile_width, self.tile_width))
        self.game_window.blit(self.Player.sprite, (player_displayed_pos_x, player_displayed_pos_y))
        
        
        pygame.display.update()

    def run_game_loop(self):
        #initialise game
        pygame.init()
        clock = pygame.time.Clock()

        self.maze.generatePath()
        self.maze.fillMaze()
        player_direction_x = 0
        player_direction_y = 0
        #main loop
        while True:
            #handle events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction_y = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction_y = 1
                    if event.key == pygame.K_RIGHT:
                        player_direction_x = 1
                    elif event.key == pygame.K_LEFT:
                        player_direction_x = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction_y = 0
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        player_direction_x = 0
            #execute logic
                        
            self.Player.move(player_direction_y, player_direction_x, self.maze_height, self.maze_width)
            #update display
            self.draw()
            clock.tick(10)

if __name__ == "__main__":
    game = Game(10,10,255)
    game.run_game_loop()