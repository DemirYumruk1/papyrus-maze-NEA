import pygame
import time
from mazearray import MazeArray
from player import Player
class Game:
    def __init__(self, maze_width, maze_height, seed):
        pygame.init()
        self.seed = seed
        self.maze = MazeArray(maze_width, maze_height, seed)
        self.maze_width = maze_width + 1 #room for the goal tiles
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
 

        self.tile_width = 32 #only need width, the tiles are square
        #tiles are 32x32 so the window must be 32 times the amount of tiles to display them all
        self.window_width = maze_width * self.tile_width
        self.window_height = maze_height * self.tile_width
        #game window size must be based on tiles
        self.game_window = pygame.display.set_mode((self.window_width, self.window_height + 100)) #+100 gives headroom for GUI

        #the player's sprite must also be proportional to the tile size
        self.Player = Player(0, round(maze_height/2), "Assets/player_normal.png", self.tile_width)

        self.seconds = 0 #goes up every second (100 ticks)
        self.score = 0 #goes up every time a green tile is pressed

        self.GUIfont = pygame.font.SysFont("comicsansms", 72)
        self.score_disp = self.GUIfont.render(f"score: {self.score}", True, (0,0,0))
        self.timer_disp = self.GUIfont.render(f"time: {(self.seconds//60):02}m:{(self.seconds % 60):02}", True, (0,0,0))


    def draw(self):
        self.game_window.fill(0) #refresh screen

        player_displayed_pos_x = self.Player.x * self.tile_width
        player_displayed_pos_y = self.Player.y * self.tile_width


        for j, row in enumerate(self.mazeArray):
            for i, tile in enumerate(row):
                colour = self.tile_id[tile[0]] #tile[0], because the tile itself contains a list ([1] instead of 1)
                pygame.draw.rect(self.game_window, colour, (i * self.tile_width, j * self.tile_width, self.tile_width, self.tile_width))
        self.game_window.blit(self.Player.sprite, (player_displayed_pos_x, player_displayed_pos_y))
        self.game_window.blit(self.score_disp, (5, self.window_height + 50))

        pygame.display.update()

    def check_tile(self, dir_x, dir_y):
        current_x = self.Player.getXpos()
        current_y = self.Player.getYpos()
        next_x = current_x + dir_x
        next_y = current_y + dir_y
        next_tile = self.maze.getTile(next_x, next_y)
        return next_tile

    def run_game_loop(self):
        #initialise game
        
        clock = pygame.time.Clock()
        self.maze.generatePath()
        self.maze.fillMaze()
        player_direction_x = 0
        player_direction_y = 0
        next_tile = 0

        #start BGM
        pygame.mixer.init()
        pygame.mixer.music.load("Assets/BGM.mp3")
        pygame.mixer.music.play(-1)

        def move(next_tile):
############################################################################################################################################
            def slip(player_direction_y, player_direction_x):
                self.Player.setFlavour(False)
                try:
                    next_tile = self.check_tile(player_direction_x, player_direction_y)
                except:
                    next_tile = [6]

                #prevent illegal movement
                if not ((next_tile == [6]) or (next_tile == [7]) or (next_tile == [8]) or (next_tile == [2] and self.Player.getFlavour())):
                    self.Player.move(player_direction_y, player_direction_x, self.maze_height -1 , self.maze_width -1)

                #exit slip physics if the end of the maze is found
                if next_tile == [0]:
                    return 

                #move twice if tile ahead is purple (this caused me so much pain)
                elif next_tile == [5]: 
                    if not ((player_direction_x, player_direction_y) == (0, 0)):
                        slip(player_direction_y, player_direction_x)
                        next_tile = self.check_tile(player_direction_x, player_direction_y) #check next tile to see if it's purple again                
###############################################################################################################################################
            if not ((next_tile == [6]) or (next_tile == [7]) or (next_tile == [8])): #check if next tile isn't electrified or red
                if not(next_tile == [2] and self.Player.getFlavour()): #check if player smells like oranges and isn't crossing water if so
                    #if these two checks are passed, then the player can move.
                    self.Player.move(player_direction_y, player_direction_x, self.maze_height -1 , self.maze_width -1)

                    if next_tile == [4]: #change flavour to orange when pressing orange tile
                        self.Player.setFlavour(True)

                    elif next_tile == [5]:
                        slip(player_direction_y, player_direction_x)
                    
                    if (next_tile == [3]):
                        self.score += 1
                        print(self.score)


        #main loops
        while True:
            #handle events

            #disable mouse inputs, as they cause green tiles to trigger
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
            pygame.event.set_blocked(pygame.MOUSEMOTION)
            events = pygame.event.get()
            
            player_direction_x = 0
            player_direction_y = 0
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction_y = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction_y = 1
                    elif event.key == pygame.K_RIGHT:
                        player_direction_x = 1
                    elif event.key == pygame.K_LEFT:
                        player_direction_x = -1
                    try: #only need to check next tile when a key is pressed
                        next_tile = self.check_tile(player_direction_x, player_direction_y)
                    except:
                        pass
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction_y = 0
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        player_direction_x = 0

            #execute logic
            move(next_tile)

            if next_tile == [0]:
                return
            
            next_tile = [1] #reset next tile
            #update display
            self.draw()
            #print(f"{self.seconds} seconds")
            self.seconds = pygame.time.get_ticks() / 1000
            clock.tick(10)

if __name__ == "__main__":
    game = Game(5,5, 123)
    game.run_game_loop()
    print(game.mazeArray)

