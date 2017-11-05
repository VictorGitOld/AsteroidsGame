import pygame

from asteroids import Asteroids
pygame.init()
# Create an object for managing the game
game = Asteroids( "Asteroids", 640, 480 )
# Start the main game loop
game.runGame()








