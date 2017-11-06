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
from polygon import Polygon
from player import Player
import time



class Asteroids( Game ):
    """
    Asteroids extends the base class Game to provide logic for the specifics of the game
    """
    def __init__(self, name, width, height):
        super().__init__( name, width, height )

        #creates the ship, a player and the lives queue
        self.ship = Ship([Point(0, 0), Point(-10, 10), Point(15, 0), Point(-10, -10)])
        self.player = Player(3)
        self.lives =[]
        self.level = 1
        self.nextLevelBool =False
        xPos=15
        for i in range(3):
            self.lives.append(Ship([Point(0, 0), Point(-10, 10), Point(15, 0), Point(-10, -10)],xPos,15))
            xPos=xPos+30
        #Creates 8 random asteroids
        self.asteroids = []
        for i in range(8):
            self.asteroids.append(Rocks(self.level))
        self.stars=[]
        for i in range(400):
            self.stars.append(Star())

        self.bullets = []

        self.dead = False
        #self.music = True
        #if self.music == True:
        #    pygame.mixer.music.load("snakeman.mp3")
        #    pygame.mixer.music.play(-1)


    def handle_input(self):
        super().handle_input()
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_LEFT] and self.ship:
            self.ship.rotate(-8)
        if keys_pressed[K_RIGHT] and self.ship:
            self.ship.rotate(8)
        if keys_pressed[K_UP] and self.ship:
            self.ship.accelerate(0.1)
        if keys_pressed[K_DOWN] and self.ship:
            self.ship.accelerate(0)
        if keys_pressed[K_SPACE] and self.ship:
            # makes it possible to only fire one bullet every n=5 frame
            if len(self.bullets)>0 and self.frame - self.bullets[len(self.bullets)-1].born <5:
                pass
            else:
                self.bullets.append(Bullet(self.ship.position, self.ship.rotation, self.frame))
            pass

    def update_simulation(self):
        """
        update_simulation() causes all objects in the game to update themselves
        """
        super().update_simulation()

        if self.ship:
            self.ship.update( self.width, self.height )

        if self.nextLevelBool==True:
            for i in range(8):
                self.asteroids.append(Rocks(self.level))
                self.nextLevelBool=False
        for asteroid in self.asteroids:
            asteroid.update( self.width, self.height )
        for star in self.stars:
            star.update( self.width, self.height )
        for bullets in self.bullets:
            bullets.update( self.width, self.height )
        self.handle_collisions()

    def render_objects(self):
        """
        render_objects() causes all objects in the game to draw themselves onto the screen
        """
        super().render_objects()
        # Render the ship if it exist:

        if self.dead==False:
            self.ship.draw( self.screen )
        # Render all the stars, if any:
        for star in self.stars:
            star.draw( self.screen )
        # Render all the asteroids, if any:
        for asteroid in self.asteroids:
            asteroid.draw( self.screen )
        # Render all the asteroids, if any:
        for lives in self.lives:
            lives.draw( self.screen )
        # Render all the bullet, if any:
        for bullet in self.bullets:
            #makes bullet disapear after n frames, lifetime set in bullets class
            count = 0
            if bullet.lifetime > self.frame:
                count = count+1
                bullet.draw( self.screen )
            else:
                self.bullets.pop(count)
                count = count + 1


        scoreFont = pygame.font.Font(None, 30)
        score = scoreFont.render("Score:"+str(self.player.score), True, (255, 0, 0))
        self.screen.blit(score, [520, 5])

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
        b = self.bullets
        countBullet = 0

        #Player will get 3 lives, lose 1 life when collision happens. dies when 3 happens
        #Player restarts in the middle. might make it to an empty spot in future
        for i in a:
            if s.collide(i):
                self.player.lives-=1
                if len (self.lives) > 0:
                    self.lives.pop()

                if self.player.lives==0:
                    self.dead=True

                else:
                    self.ship.position.x=self.screen.get_width()/2
                    self.ship.position.y = self.screen.get_height()/2
                    #self.ship.angular_velocity(0)
                    self.ship.pull=Point(0,0)

                #self.music = False
                #if self.music == False:
                #    pygame.mixer.music.load("GameOver.mp3")
                #    pygame.mixer.music.play(1)
                #    time.sleep(3)
                #    self.running = False
                #else:
                #    pass

        #Bullet collision, player gets score,
        for i in b:
            #creates a polygon bullet at the location of the real bullet which can collide with asteroids
            #removes the bullet and the asteroid
            tempPositionX = i.position.x
            tempPositionY = i.position.y
            tempPoints=[Point(5, 5), Point(-5, 5), Point(-5, -5), Point(5, -5)]
            tempBullet=Polygon(tempPoints,tempPositionX,tempPositionY,0,Point(0,0),0)
            count=0
            for j in a:
                if tempBullet.collide(j):

                    self.asteroids.pop(count)

                    self.bullets.pop(countBullet)
                    self.player.score=self.player.score+50

                count += 1
            countBullet +=1

        if len(self.asteroids)==0:
            self.level=self.level+1
            self.nextLevelBool=True
        else:
            pass

