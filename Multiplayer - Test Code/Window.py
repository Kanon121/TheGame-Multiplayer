import pygame 
class Window:
    def CreateWindow(self, height, width):
        self.size = width, height
        self.screen = pygame.display.set_mode(self.size)
    def RenderWindow(self, color):
        if color == "black":
            color = 0,0,0
        self.screen.fill(color)
