import Globals as gb
import os
all_projectiles = []
class Projectile():
    def __init__(self, image, x, y, direction):
        self.setup(image) 
        self.pic = image
        self.rect = self.image.get_rect()
        self.direction = direction
        self.speed = 15
        all_projectiles.append(self)
        self.rect.x = x
        self.rect.y = y
        self.flying = False
    

    
    def setup(self, image):
        img_file = os.path.join('img', image)
        self.image = gb.pygame.image.load(img_file)
        
   
def Update():

    if all_projectiles:
        for pro in all_projectiles:
            gb.maps.checkCollisions(pro, "projectile")
            if pro.direction == "left":
                pro.rect.x -= pro.speed
            if pro.direction == "right":
                pro.rect.x += pro.speed
            if pro.direction == "up":
                pro.rect.y -= pro.speed
            if pro.direction == "down":
                pro.rect.y += pro.speed
def Render():
    for pro in all_projectiles:
    
        gb.window.screen.blit(pro.image, (pro.rect.x - gb.cam.rect.x,
            pro.rect.y - gb.cam.rect.y))