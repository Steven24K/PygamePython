import pygame
import sys
import random
import components as c
import color as clr
import Text
import button


pygame.init()
pygame.font.init()

#The class Game3 is called a singleton class or singleton object, that means that there can only
#exist one instance of this object "Game3". In here we we define the entire game we want to build,
#in the def __init__ we initialize the attributes that make up the game, in example:
#Title, game window size(height x width), a default font, background color and all the players and enemy objects

#The run method (def run:) specifies the game loop, this loop is responsible for everthing what happens in the game.
#The things this method does are:
#Check for keyboard input, draw the characters on the screen and all the character updates and opperations such as jump, move and gravity

class Game3:
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
        self.StartText = Text.Text(self.Color.Black, self.DefaultFont, "This pygame template provides an easy way to quickly build a game in Python.")
        self.NextLine = Text.Text(self.Color.Black, self.DefaultFont, "Why do the same thing over and over again when it allready exists!!!")

        #Create all game characters here
        self.Player1 = c.Component(c.Position(400,100), "enemy.png")

        
        #Create a button
        self.ExitButton = button.Button(300,250, 50,200, self.Color.Red, Text.Text(self.Color.Black, self.DefaultFont, "Next"))
        

    def update(self):
        self.Player1.update(20,0)
        self.Player1.horizontal_screen_wrap(self.Width)

        self.ExitButton.update()

    def draw(self): 
        #Set the background color of the pygame window, HINT: See what happens when you remove this line
        self.Screen.fill(self.Color.Turquoise)

        #Player drawing and animation
        self.Player1.draw(self.Screen)

            
        #Draw start text
        self.StartText.draw(self.Screen, 100, 30)
        self.NextLine.draw(self.Screen, 100, 50)

        #Draw buttons
        self.ExitButton.draw(self.Screen)


    def run(self):
        while True:
            for event in pygame.event.get():
              if event.type == pygame.QUIT: sys.exit()

            self.update()
            self.draw()

            if self.ExitButton.clicked():
                break

            self.Clock.tick(30)
            pygame.display.flip()
            pygame.display.set_caption(self.Title)


#To test only a single game, uncomment this code and run python <GAME_NAME>.pygame
#Short cut: CTRL + K + C (Comment) CTRL + K + U (uncomment)
if __name__ == "__main__":
    test_game = Game3("Test instance", 1200,600)
    test_game.run()
