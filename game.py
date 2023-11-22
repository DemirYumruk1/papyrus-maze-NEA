import pygame
from mazearray import MazeArray
class Game:
    def __init__(self, maze_width, maze_height, seed):

        self.seed = seed

        self.maze = MazeArray(maze_width, maze_height)
        #game window size must be based on tiles
        #self.game_window = pygame.display.set_mode((self.x,self.y))

    def run_game_loop():
        pass