import pygame
import pygame.transform

class Component:
    def __init__(self, position, image, speed = 0):
        self.Score = 0
        self.Speed = speed
        self.Image = pygame.image.load(image)
        self.ImageRect = self.Image.get_rect()
        self.ImageRect.x = position.X
        self.ImageRect.y = position.Y
    def draw(self, screen):
        screen.blit(self.Image, (self.ImageRect))
    def update(self, xspeed, yspeed):
        self.ImageRect = self.ImageRect.move(xspeed,yspeed)
    def gravity(self, screen_height, strenght):
        if self.ImageRect.y + self.Image.get_rect().height < screen_height:
            self.ImageRect = self.ImageRect.move(0, strenght)
    def jump(self, jump_height, screen_height):
        if self.ImageRect.y > 0:
            self.ImageRect = self.ImageRect.move(0,-jump_height)
    def horizontal_screen_wrap(self, screen_width):
        if self.ImageRect.x + self.ImageRect.width < 0:
            self.ImageRect.x = screen_width
        if self.ImageRect.x > screen_width:
            self.ImageRect.x = -self.ImageRect.width
    def vertical_screen_wrap(self, screen_height):
        if self.ImageRect.y + self.ImageRect.height < 0:
            self.ImageRect.y = screen_height
        if self.ImageRect.y > screen_height:
            self.ImageRect.y = -self.ImageRect.height
    def display_score(self, screen, font, text_color):
        screen.blit(font.render("Score: " + str(self.Score),False,text_color),(self.ImageRect.x, self.ImageRect.y))
    def display_position(self, screen, font, text_color):
        screen.blit(font.render("(x: " + str(self.ImageRect.x) + ",y: " + str(self.ImageRect.y) + ")", False, text_color), (self.ImageRect.x, self.ImageRect.y-40))
    def intersection(self, x, y, height, width):
        return (self.ImageRect.x + self.ImageRect.width > x and self.ImageRect.x < x + width and self.ImageRect.y + self.ImageRect.height > y and self.ImageRect.y < y + height)


                   
        
class Position:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    def __str__(self):
        return "(" + str(self.X) + "," + str(self.Y) + ")"