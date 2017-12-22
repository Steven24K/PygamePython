import pygame
import sys
import random
import components as c
import color as clr

pygame.init()
pygame.font.init()

#The class MainGame is called a singleton class or singleton object, that means that there can only
#exist one instance of this object "MainGame". In here we we define the entire game we want to build,
#in the def __init__ we initialize the attributes that make up the game, in example:
#Title, game window size(height x width), a default font, background color and all the players and enemy objects

#The run method (def run:) specifies the game loop, this loop is responsible for everthing what happens in the game.
#The things this method does are:
#Check for keyboard input, draw the characters on the screen and all the character updates and opperations such as jump, move and gravity

class MainGame:
    def __init__(self, title, width, height):
        self.Title = title
        self.Height = height
        self.Width = width
        self.Screen = pygame.display.set_mode((self.Width, self.Height))

        self.DefaultFont = pygame.font.SysFont(None,30)
        
        #This color is a refrence to the color object, in there all different colors are defined
        self.Color = clr.Color()

        #Create all game characters here
        self.Player1 = c.Character(c.Position(200,250), "knight.png")
        self.Enemy1 = c.Character(c.Position(50,180) , "enemy.png", 5)
        self.Enemy2 = c.Character(c.Position(100,230) , "enemy.png", 5)
        self.Enemy3 = c.Character(c.Position(150,280) , "enemy.png", 5)

    def run(self):
        while True:
            for event in pygame.event.get():
              if event.type == pygame.QUIT: sys.exit()

            self.Screen.fill(self.Color.White)
            
            #Get keyboard input, checks if a certain key is pressed or not
            keys = pygame.key.get_pressed()

            ################################################################
            ####################START FOR YOUR GAME#########################
            ################################################################

            #Player opperations, draw, update, set gravity, wrap screen and display score
            self.Player1.draw(self.Screen)
            self.Player1.horizontal_screen_wrap(self.Width)
            self.Player1.vertical_screen_wrap(self.Height)
            self.Player1.display_score(self.Screen, self.DefaultFont, self.Color.Green)
            self.Player1.display_position(self.Screen, self.DefaultFont, self.Color.Blue)
           
            if keys[pygame.K_LEFT]:
                self.Player1.update(-2,0)
            if keys[pygame.K_RIGHT]:
                self.Player1.update(2,0)
            if keys[pygame.K_UP]:
                self.Player1.update(0, -2)
            if keys[pygame.K_DOWN]:
                self.Player1.update(0, 2)

            if self.Player1.intersection(self.Enemy1.ImageRect.x, self.Enemy1.ImageRect.y, self.Enemy1.ImageRect.height, self.Enemy1.ImageRect.width):
                self.Player1.Score += 1
                self.Enemy1.ImageRect.x = random.randint(0, self.Width - self.Enemy1.ImageRect.width)
                self.Enemy1.ImageRect.y = random.randint(0, self.Height -self.Enemy1.ImageRect.height)

            #Enemy opperations draw, update and wrap screen
            self.Enemy1.draw(self.Screen)
            self.Enemy1.horizontal_screen_wrap(self.Width)
            self.Enemy1.display_position(self.Screen, self.DefaultFont, self.Color.Blue)

            if self.Player1.intersection(self.Enemy2.ImageRect.x, self.Enemy2.ImageRect.y, self.Enemy2.ImageRect.height, self.Enemy2.ImageRect.width):
                self.Player1.Score += 1
                self.Enemy2.ImageRect.x = random.randint(0, self.Width - self.Enemy1.ImageRect.width)
                self.Enemy2.ImageRect.y = random.randint(0, self.Height -self.Enemy1.ImageRect.height)

            #Enemy opperations draw, update and wrap screen
            self.Enemy2.draw(self.Screen)
            self.Enemy2.horizontal_screen_wrap(self.Width)
            self.Enemy2.display_position(self.Screen, self.DefaultFont, self.Color.Blue)

            if self.Player1.intersection(self.Enemy3.ImageRect.x, self.Enemy3.ImageRect.y, self.Enemy3.ImageRect.height, self.Enemy3.ImageRect.width):
                self.Player1.Score += 1
                self.Enemy3.ImageRect.x = random.randint(0, self.Width - self.Enemy3.ImageRect.width)
                self.Enemy3.ImageRect.y = random.randint(0, self.Height -self.Enemy3.ImageRect.height)

            #Enemy opperations draw, update and wrap screen
            self.Enemy3.draw(self.Screen)
            self.Enemy3.horizontal_screen_wrap(self.Width)
            self.Enemy3.display_position(self.Screen, self.DefaultFont, self.Color.Blue)

            pygame.display.flip()
            pygame.display.set_caption(self.Title)

#Create a new game and run the program
game = MainGame("My pygame",1200,600)
game.run()