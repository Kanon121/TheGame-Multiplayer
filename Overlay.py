import Globals as gb
import os
class Overlay():
    def __init__(self):
        self.font = gb.pygame.font.SysFont("monospace", 30)
        self.heartlist = [] 
        heartPath = os.path.join('img', 'heart.png')
        self.heartImage = gb.pygame.image.load(heartPath)

    def update(self):
        pass # TO DO, PUT KEYS AND HEARTS IN HERE

    def displayHearts(self):
        maxHearts = gb.player.maxhearts 
        currentHearts = gb.player.hearts      
        self.heartlist = []
        while currentHearts > 0:
            heart = self.heartImage.get_rect()
            heart.x = currentHearts * 20 - 10
            heart.y = 10
            currentHearts -= 1
            self.heartlist.append(heart)
        for heart in self.heartlist:
            gb.window.screen.blit(self.heartImage, (heart.x, heart.y))
                

    def render(self):
        keys = gb.player.keys
        keyText = self.font.render("Keys: "+str(keys), 1, (255,255,0))
        gb.window.screen.blit(keyText, (10, 50))
        self.displayHearts()






