import sys
import random
import pygame

from pygame.locals import *

from game import Game
from ship import Ship
from point import Point
from rocks import Rocks
from star import Star
from bullet import Bullet
import time



class Asteroids( Game ):
    """
    Asteroids extends the base class Game to provide logic for the specifics of the game
    """
    def __init__(self, name, width, height):
        super().__init__( name, width, height )

        self.ship = Ship([Point(0, 0), Point(-10, 10), Point(15, 0), Point(-10, -10)])

        self.asteroids = []
        for i in range(8):
            self.asteroids.append(Rocks(i%2))

        self.stars=[]
        for i in range(400):
            self.stars.append(Star())

        self.bullets = []

        self.dead = False
        self.music = True
        if self.music == True:
            pygame.mixer.music.load("snakeman.mp3")
            pygame.mixer.music.play(-1)


    def handle_input(self):
        super().handle_input()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_LEFT] and self.ship:
            self.ship.rotate(-1.5)
        if keys_pressed[K_RIGHT] and self.ship:
            self.ship.rotate(1.5)
        if keys_pressed[K_UP] and self.ship:
            self.ship.accelerate(0.01)
        if keys_pressed[K_DOWN] and self.ship:
            self.ship.accelerate(0)
        if keys_pressed[K_SPACE] and self.ship:
            if len(self.bullets) >= 1:
                del self.bullets[0]
                self.bullets.append(Bullet(self.ship.position, self.ship.rotation, self.frame))
            else:
                self.bullets.append(Bullet(self.ship.position, self.ship.rotation, self.frame))
            # TODO: should create a bullet when the user fires






    def update_simulation(self):
        """
        update_simulation() causes all objects in the game to update themselves
        """
        super().update_simulation()

        if self.ship:
            self.ship.update( self.width, self.height )
        for asteroid in self.asteroids:
            asteroid.update( self.width, self.height )
        for star in self.stars:
            star.update( self.width, self.height )
        for bullets in self.bullets:
            bullets.update(self.width, self.height)
        # TODO: should probably call update on our bullet/bullets here
        # TODO: should probably work out how to remove a bullet when it gets old
        self.handle_collisions()

    def render_objects(self):
        """
        render_objects() causes all objects in the game to draw themselves onto the screen
        """
        super().render_objects()
        # Render the ship:

        if self.ship:
            self.ship.draw( self.screen )
        # Render all the stars, if any:
        for star in self.stars:
            star.draw( self.screen )
        # Render all the asteroids, if any:
        for asteroid in self.asteroids:
            asteroid.draw( self.screen )
        # Render all the bullet, if any:
        for bullet in self.bullets:
            bullet.draw( self.screen )

        if self.dead:
            font = pygame.font.Font(None, 100)
            text = font.render("Game Over", True, (255,0,0))
            text_rect = text.get_rect()
            text_x = self.screen.get_width()/2 - text_rect.width / 2
            text_y = self.screen.get_height() / 2 - text_rect.height / 2
            self.screen.blit(text, [text_x, text_y])



    def handle_collisions(self):
        s = self.ship
        a = self.asteroids
        #Game will quit if user collide with a rock.
        for i in a:
            if s.collide(i):
                self.dead = True
                self.music = False
                if self.music == False:
                    pygame.mixer.music.load("GameOver.mp3")
                    pygame.mixer.music.play(1)
                    time.sleep(3)
                    self.running = False
                else:
                    pass


        """
        handle_collisions() should check:
            - if our ship has crashed into an asteroid (the ship gets destroyed - game over!)
            - if a bullet has hit an asteroid (the asteroid gets destroyed)
        :return: 
        """
        # TODO: implement collission detection,
        #       using the collission detection methods in all of the shapes
        pass
