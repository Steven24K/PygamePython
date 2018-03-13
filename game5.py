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

class Game5:
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


    def update(self):
        #Your update logic here
        x = 0

    def draw(self): 
        #You drawing logic here
        self.Screen.fill(self.Color.Red)

    def run(self):
        #Change False to True, this just to skip this empty game
        while False:
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
    test_game = Game5("Test instance", 1200,600)
    test_game.run()