import pygame
from mazearray import MazeArray
class Game:
    def __init__(self, maze_width, maze_height, seed):
        self.seed = seed
        self.maze = MazeArray(maze_width, maze_height, seed)

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
        #tiles are 8x8 so the window must be 8 times the amount of tiles to display them all
        self.window_width = maze_width * 8
        self.window_height = maze_height * 8

        #game window size must be based on tiles
        self.game_window = pygame.display.set_mode((self.window_width,self.window_height))

    def run_game_loop():
        pass