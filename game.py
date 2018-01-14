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
        self.Player1 = c.Component(c.Position(200,250), "knight.png")

        #This is a list/array of all enemies, at initialization there is only one enemy in the list
        self.Enemies = []
        self.Enemies.append(c.Component(c.Position(50,250), "enemy.png"))

    def run(self):
        while True:
            for event in pygame.event.get():
              if event.type == pygame.QUIT: sys.exit()

            #Set the background color of the pygame window, HINT: See what happens when you remove this line
            self.Screen.fill(self.Color.White)
            
            #Get keyboard input, checks if a certain key is pressed or not
            keys = pygame.key.get_pressed()


            #Player opperations, draw, update, set gravity, wrap screen and display score
            self.Player1.draw(self.Screen)
            self.Player1.horizontal_screen_wrap(self.Width)
            self.Player1.vertical_screen_wrap(self.Height)
            self.Player1.display_score(self.Screen, self.DefaultFont, self.Color.Green)
            self.Player1.display_position(self.Screen, self.DefaultFont, self.Color.Blue)
           
           #Keyboard checks if a certain key is pressed the player will respond to that
            if keys[pygame.K_LEFT]:
                self.Player1.update(-2,0)
            if keys[pygame.K_RIGHT]:
                self.Player1.update(2,0)
            if keys[pygame.K_UP]:
                self.Player1.update(0, -2)
            if keys[pygame.K_DOWN]:
                self.Player1.update(0, 2)

            #This for-loop draws all enemies on the screen and checks for all enemies if the main player has an intersection with 
            #on of them,
            for enemy in self.Enemies:
                enemy.draw(self.Screen)
                if self.Player1.intersection(enemy.ImageRect.x, enemy.ImageRect.y, enemy.ImageRect.height, enemy.ImageRect.width):
                    self.Player1.Score += 1
                    enemy.ImageRect.x = random.randint(0, self.Width - enemy.ImageRect.width)
                    enemy.ImageRect.y = random.randint(0, self.Height -enemy.ImageRect.height)
                    self.Enemies.append(c.Component(c.Position(random.randint(0, self.Width - enemy.ImageRect.width),random.randint(0, self.Height -enemy.ImageRect.height)),"enemy.png"))

            #Clears the enemy list if it becomes to big, if there to many enemies the game will become slow,
            #Question to ask yourself: Why is the game becomming slow if there are to many enemies?
            #Todo: Is there a way to fix this?
            if len(self.Enemies) > 10:
                 self.Enemies.clear()
                 self.Enemies.append(c.Component(c.Position(random.randint(0, self.Width - enemy.ImageRect.width),random.randint(0, self.Height -enemy.ImageRect.height)),"enemy.png"))

            pygame.display.flip()
            pygame.display.set_caption(self.Title)

#Create a new game and run the program
game = MainGame("My pygame",1200,600)
game.run()