import pygame

class Text:
    #A Text object, this is to draw text on the pygame screen
    def __init__(self, color, font, message):
        self.Color = color
        self.Message = message
        self.Font = font
    def draw(self, screen, x, y):
        screen.blit(self.Font.render(self.Message,False,self.Color),(x, y))