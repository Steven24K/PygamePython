import pygame 
import sys
import components as c
import color as clr
import Text
import button

pygame.init()
pygame.font.init()

#The class MainMenu is called a singleton class or singleton object, that means that there can only
#exist one instance of this object "MainMenu". In here we we define the entire game we want to build,
#in the def __init__ we initialize the attributes that make up the game, in example:
#Title, game window size(height x width), a default font, background color and all the players and enemy objects

#The run method (def run:) specifies the game loop, this loop is responsible for everthing what happens in the game.
#The things this method does are:
#Check for keyboard input, draw the characters on the screen and all the character updates and opperations such as jump, move and gravity

class MainMenu:
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
        self.StartText = Text.Text(self.Color.Black, self.DefaultFont, "Welcom to my pygame template!!!")
        
        #Create all game characters here
        self.Player1 = c.Component(c.Position(400,100), "enemy.png")

        
        #Create a button
        self.ExitButton = button.Button(300,250, 50,200, self.Color.Red, Text.Text(self.Color.Black, self.DefaultFont, "Exit"), lambda  : sys.exit())
        self.StartButton = button.Button(600, 250, 50, 200, self.Color.Green, Text.Text(self.Color.Black, self.DefaultFont, "Start"))

    def update(self):
        #Todo: Make the player move on the screen
        self.Player1.update(5,0)
        self.Player1.horizontal_screen_wrap(self.Width)

        #Todo: Make the exit button work
        self.ExitButton.update()


    def draw(self): 
        #Set the background color of the pygame window, HINT: See what happens when you remove this line
        self.Screen.fill(self.Color.Purple)

        #Player drawing and animation
        self.Player1.draw(self.Screen)
            
        #Draw start text
        self.StartText.draw(self.Screen, 400, 30)

        #Draw buttons
        self.ExitButton.draw(self.Screen)
        self.StartButton.draw(self.Screen)

    def run(self):
        while True:
            for event in pygame.event.get():
              if event.type == pygame.QUIT: sys.exit()
                  
            self.update()
            self.draw()

            if self.StartButton.clicked():
                #When the start button is clicked the game will end and the next game in the Que will start
                break

            #Make the game run at 30frames per seccond (30fps)
            self.Clock.tick(30)
            pygame.display.flip()
            pygame.display.set_caption(self.Title)


#To test only a single game, uncomment this code and run python <GAME_NAME>.pygame
#Short cut: CTRL + K + C (Comment) CTRL + K + U (uncomment)
if __name__ == "__main__":
    test_game = MainMenu("Test instance", 1200,600)
    test_game.run()
