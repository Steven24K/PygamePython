import pygame
import sys
import random
import components as c
import color as clr
import Text
import button
import math

pygame.init()
pygame.font.init()

#The class Game4 is called a singleton class or singleton object, that means that there can only
#exist one instance of this object "Game4". In here we we define the entire game we want to build,
#in the def __init__ we initialize the attributes that make up the game, in example:
#Title, game window size(height x width), a default font, background color and all the players and enemy objects

#The run method (def run:) specifies the game loop, this loop is responsible for everthing what happens in the game.
#The things this method does are:
#Check for keyboard input, draw the characters on the screen and all the character updates and opperations such as jump, move and gravity

class Game4:
    def __init__(self, title, width, height):
        self.Title = title
        self.Height = height
        self.Width = width
        self.Screen = pygame.display.set_mode((self.Width, self.Height))

        #This is to initialize the framerate (fps)
        self.Clock = pygame.time.Clock()

        #This color is a refrence to the color object, in there all different colors are defined
        self.Color = clr.Color()
        self.DefaultFont = pygame.font.SysFont(None,30)

        #Initialize text messages
        self.InfoText = Text.Text(self.Color.Red, self.DefaultFont, "COUNT TO 10 | Click the button to increment the counter and finish the game!!!")

        
        #Create a button
        self.CountButton = button.Button(100,250, 50,200, self.Color.Yellow, Text.Text(self.Color.Black, self.DefaultFont, "Click me!"))
       
        #Initialize the counter to 0
        self.Counter = 0

        #Store the counter in a text object
        self.CounterText = Text.Text(self.Color.Black, self.DefaultFont, str(self.Counter))
        

    def update(self):
        #When we click the button the counter will be updated  
        if self.CountButton.clicked():
            self.Counter += 0.3
            #We also must update the text object in order to display the correct and updated counter
            self.CounterText = Text.Text(self.Color.Black, self.DefaultFont, str(math.ceil(self.Counter))) #HINT: See what happens when you remove math.ceil
                                                                                                           #For better understanding of the pygame runtime

    def draw(self): 
        #Set the background color of the pygame window, HINT: See what happens when you remove this line
        self.Screen.fill(self.Color.Blue)
          
        #Draw start text
        self.CounterText.draw(self.Screen, 500, 30)
        self.InfoText.draw(self.Screen, 50, 80)

        #Draw buttons
        self.CountButton.draw(self.Screen)


    def run(self):
        while self.Counter <= 10:
            for event in pygame.event.get():
              if event.type == pygame.QUIT: sys.exit()

            self.update()
            self.draw()


            self.Clock.tick(30)
            pygame.display.flip()
            pygame.display.set_caption(self.Title)


#To test only a single game, uncomment this code and run python <GAME_NAME>.pygame
#Short cut: CTRL + K + C (Comment) CTRL + K + U (uncomment)
# test_game = Game4("Test instance", 1200,600)
# test_game.run()