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
        self.StartText = Text.Text(self.Color.Black, self.DefaultFont, "Make the player move on the screen, up, down, left and right!")
        self.NextLine = Text.Text(self.Color.Black, self.DefaultFont, "Why do the same thing over and over again when it allready exists!!!")

        #Create all game characters here
        self.Player1 = c.Component(c.Position(400,100), "enemy.png")
        self.Apple = c.Component(c.Position(100,100),"apple.png")
       
        self.AppleCounter = 0
        self.Score = Text.Text(self.Color.Black, self.DefaultFont, "Apple Counter: " + str(self.AppleCounter))

        
       
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.Player1.update(-5,0)
        if keys[pygame.K_RIGHT]:
            self.Player1.update(5,0)
        #Todo: Make the player move up and Down 

        if self.Player1.intersection(self.Apple.ImageRect.x, self.Apple.ImageRect.y, self.Apple.ImageRect.height, self.Apple.ImageRect.width):
            self.Apple.ImageRect.x = random.randint(0, self.Width-self.Apple.ImageRect.width)
            self.Apple.ImageRect.y = random.randint(0, self.Height-self.Apple.ImageRect.height)
            self.AppleCounter += 1

        #Todo: Update the AppleCounter Text
        
        self.Player1.horizontal_screen_wrap(self.Width)
        self.Player1.vertical_screen_wrap(self.Height)


    def draw(self): 
        #Set the background color of the pygame window, HINT: See what happens when you remove this line
        self.Screen.fill(self.Color.Turquoise)

        #Player drawing and animation
        self.Player1.draw(self.Screen)

        #Draw apple
        self.Apple.draw(self.Screen)    
        
        #Draw start text
        self.StartText.draw(self.Screen, 500, 30)
        self.NextLine.draw(self.Screen, 500, 50)
        self.Score.draw(self.Screen, 50,50)



    def run(self):
        #Make the game end when the apple counter is 10
        while True:
            for event in pygame.event.get():
              if event.type == pygame.QUIT: sys.exit()

            self.update()
            self.draw()


            self.Clock.tick(30)
            pygame.display.flip()
            pygame.display.set_caption(self.Title)


#To test only a single game, uncomment this code and run python <GAME_NAME>.pygame
#Short cut: CTRL + K + C (Comment) CTRL + K + U (uncomment)
if __name__ == "__main__":
    test_game = Game3("Test instance", 1200,600)
    test_game.run()
