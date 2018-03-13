import pygame
import sys
import components as c
import color as clr
import Text
import button

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
        #The basic parameters wich make up the game
        self.Title = title
        self.Height = height
        self.Width = width
        self.Screen = pygame.display.set_mode((self.Width, self.Height))

        #This is to initialize the framerate (fps)
        self.Clock = pygame.time.Clock()

        #This color is a refrence to the color object, in there all different colors are defined
        self.Color = clr.Color()
        self.DefaultFont = pygame.font.SysFont(None,30)

        self.InfoText = Text.Text(self.Color.Black, self.DefaultFont, "Score 3 points to go to the next level, press space to fly!")

        #Create all game characters here
        self.Player1 = c.Component(c.Position(400,250), "enemy.png")
        
        #Empty list of enemies, this will be filled during the game 
        #This is a special kind of list called an array, each element in the array has an unique Index
        #indeces start from 0, by calling Enemies[3] you call enemy in position number 3
        #!!!!BECAREFULL WITH THE BOUNDS: When the index does not exist you will get an error, always check if the IndexError
        #exists before calling it.
        self.Enemies = []


    def update(self):
        #Get keyboard input, checks if a certain key is pressed or not and get mouse Position
        keys = pygame.key.get_pressed()


        #Player opperations
        self.Player1.gravity(self.Height, 10)
        if keys[pygame.K_SPACE] and self.Player1.ImageRect.y > 0:
            self.Player1.jump(20, self.Height)

        #Enemy opperations
        if len(self.Enemies) < 1: self.Enemies.append(c.Component(c.Position(self.Width-100, 300), "knight.png"))

        for enemy in self.Enemies:       
            enemy.gravity(self.Height, 10)
            enemy.update(-25,0)

            if enemy.ImageRect.x < 0: self.Enemies.remove(enemy)
            if enemy.intersection(self.Player1.ImageRect.x, self.Player1.ImageRect.y, self.Player1.ImageRect.height, self.Player1.ImageRect.width):
                self.Player1.Score -= 1
                self.Player1.jump(200, self.Height)
            if enemy.ImageRect.x == self.Player1.ImageRect.x: 
                self.Player1.Score += 1

    def draw(self):
        #Set the background color of the pygame window, HINT: See what happens when you remove this line
        self.Screen.fill(self.Color.White)
        self.InfoText.draw(self.Screen, 120, 80)
            
        #Draw Player 1
        self.Player1.draw(self.Screen)
        self.Player1.display_position(self.Screen, self.DefaultFont, self.Color.Green)
        self.Player1.display_score(self.Screen, self.DefaultFont, self.Color.Red)

        #Draw all enemies in the list
        for enemy in self.Enemies:
            enemy.draw(self.Screen)
            enemy.display_position(self.Screen, self.DefaultFont, self.Color.Blue)

    def run(self):
        #The game will end when the score reaches 3
        while self.Player1.Score < 3:
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
    test_game = MainGame("Test instance", 1200,600)
    test_game.run()   

