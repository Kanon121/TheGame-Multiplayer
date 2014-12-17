
import Globals as gb
class Camera(object):
    def __init__(self, x, y, screen_width, screen_height):
        self.rect = gb.pygame.Rect(x, y, screen_width, screen_height)
    def update(self, edit, player):
        if not edit:
            self.rect.center = player.rect.x, player.rect.y    

