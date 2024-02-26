import pygame
from mazearray import MazeArray
from player import Player
class Game:
    def __init__(self, maze_width, maze_height, seed):
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
        self.game_window = pygame.display.set_mode((self.window_width,self.window_height))

        #the player's sprite must also be proportional to the tile size
        self.Player = Player(0, maze_height/2, "Assets/player_normal.png", self.tile_width, False)

        self.score = 0 #goes up every time a green tile is pressed

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

    def check_tile(self, dir_x, dir_y):
        current_x = self.Player.getXpos()
        current_y = self.Player.getYpos()
        next_x = current_x + dir_x
        next_y = current_y + dir_y
        next_tile = self.maze.getTile(next_x, next_y)
        #test statements
        print("current x: ")
        print(current_x)
        print("current y:")
        print(current_y)
        print("next x: ")
        print(next_x)
        print("next y: ")
        print(next_y)
        return next_tile

    def run_game_loop(self):
        #initialise game
        pygame.init()
        clock = pygame.time.Clock()

        self.maze.generatePath()
        self.maze.fillMaze()
        player_direction_x = 0
        player_direction_y = 0
        next_tile = 0

        def move(next_tile): 
            #checking tiles then moving the player is a function call 
            #purple tiles require checks to be performed twice. this will save me from copy pasting the same check twice.

            if not ((next_tile == [6]) or (next_tile == [7]) or (next_tile == [8])): #check if next tile isn't electrified or red

                if not(next_tile == [2] and self.Player.getFlavour()): #check if player smells like oranges and isn't crossing water if so

                    #if these two checks are passed, then the player can move.
                    self.Player.move(player_direction_y, player_direction_x, self.maze_height -1 , self.maze_width -1, next_tile)

                    if next_tile == [4]: #change flavour to orange when pressing orange tile
                        self.Player.setFlavour(True)

                    elif next_tile == [3]:
                        self.score += 1

                    elif next_tile == [5]:
                        self.Player.setFlavour(False)
                        while next_tile == [5]: #while loop is because multiple purples may be in a row, we want the player to slide across all.
                            next_tile = self.check_tile(player_direction_x, player_direction_y) #check next tile to see if it's purple again
                            if not ((next_tile == [6]) or (next_tile == [7]) or (next_tile == [8])):
                                if not(next_tile == [2] and self.Player.getFlavour()):
                                    self.Player.move(player_direction_y, player_direction_x, self.maze_height -1 , self.maze_width -1, next_tile)
                                    
                        
            
        #main loops
        while True:
            #handle events
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
                try:
                    next_tile = self.check_tile(player_direction_x, player_direction_y)
                except:
                    pass
            move(next_tile)
            #update display
            self.draw()
            clock.tick(10)

if __name__ == "__main__":
    game = Game(10,10,255)
    game.run_game_loop()
    print(game.mazeArray)