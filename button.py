import pygame
import pygame.rect
import Text

class Button:
    def __init__(self, x, y, height, width, color, text, action = None):
        self.X = x
        self.Y = y
        self.Height = height
        self.Width = width
        self.Color = color
        self.Text = text
        self.Action = action
    def draw(self, screen):
        pygame.draw.rect(screen, self.Color, pygame.rect.Rect(self.X, self.Y, self.Width, self.Height))
        self.Text.draw(screen, self.X + (self.Width//2), self.Y + (self.Height//2))
    def update(self):
        #Invokes the action of the button if the action is set and if the button is clicked
        if not self.Action == None:
            mouse = pygame.mouse.get_pos()
            if (self.X + self.Width > mouse[0] and self.X < mouse[0] and self.Y + self.Height > mouse[1] and self.Y < mouse[1]):
               if pygame.mouse.get_pressed()[0]: self.Action()
            else:
                self.Color
    def clicked(self):
        #Returns true when the button is clickked
        mouse = pygame.mouse.get_pos()
        if (self.X + self.Width > mouse[0] and self.X < mouse[0] and self.Y + self.Height > mouse[1] and self.Y < mouse[1]) and pygame.mouse.get_pressed()[0]:
             return True
        else:
             return False
