import pygame
import random
from game import Game
import time

width = int(input("enter width: "))
height = int(input("enter height: "))
seed = int(input("Enter a seed (0 for random): "))
if seed == 0:
    seed = int(time.time()) #this will give a different seed every execution unless user can stop time.

instance = Game(width, height, seed)

instance.run_game_loop()