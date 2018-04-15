import pygame
import sys
import random
import components as c
import color as clr
import Text
import button
import math
import time


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

        #Images
        self.Car = c.Component(c.Position(500, 500), "car.jpg")
        self.Obstacles = []


    def update(self):
        #Your update logic here
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.Car.update(-10,0)
        if keys[pygame.K_RIGHT]:
            self.Car.update(10,0)
        
        self.Car.horizontal_screen_wrap(self.Width)

        if len(self.Obstacles) < 1:
            self.Obstacles.append(c.Component(c.Position(random.randint(20, self.Width-40),0) , "truck.jpg"))
        
        for obstacle in self.Obstacles:
            obstacle.update(0, 20)
            if obstacle.ImageRect.y > self.Height:
                self.Obstacles.remove(obstacle)
            if self.Car.intersection(obstacle.ImageRect.x, obstacle.ImageRect.y, obstacle.ImageRect.height, obstacle.ImageRect.height):
                print("Game Over")
                sys.exit()

    def draw(self): 
        #You drawing logic here
        self.Screen.fill(self.Color.Red)
        self.Car.draw(self.Screen)
        for obstacle in self.Obstacles:
            obstacle.draw(self.Screen)

    def run(self):
        #Change False to True, this just to skip this empty game
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
    test_game = Game5("Test instance", 600,800)
    test_game.run()