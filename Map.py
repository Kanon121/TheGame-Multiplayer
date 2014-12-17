import Globals as gb
import ConfigParser
import os


class AddBlockType(object):
    def __init__(self):
        self.load_file()
    def load_file(self, filename="level.map"):
        self.all_types = []
        self.key = {}
        parser = ConfigParser.ConfigParser()
        parser.read(filename)
        self.all_types = parser.get("level", "level").split("\n")

        

new_blocks = []
def RenderMap():
    x = 0
    y = 0
    tile_x = 0
    tile_y = 0
    walls = []
    for row in gotTypes.all_types:
        for block in row:
          
           if block == '.':
                block = Blocks(0, x, y, 'sand.png',  False)
           
           if block == '#':
                block = Blocks(1, x, y, 'wall.png', True)
                                      
           if block == 'S':
                block = Blocks(2, x, y, 'stairsBroken.png', 
                    False)
                                           
           if block == "s":
                block = Blocks(3, x, y, 'stairsDown.png', 
                    False)                                         
           
           if block == "t":
                block = Blocks(4, x, y, 'torch.png', False)
           
           if block == "!":
                block = Blocks(5, x, y, 'door_open1.png', False)
           if block == "@":
                block = Blocks(6, x, y, 'door_open2.png', False)
           if block == "%":
                block = Blocks(7, x, y, 'door_closed1.png', True)
           if block == "$":
                block = Blocks(8, x, y, 'door_closed2.png', True)

           if block == "^":
                block = Blocks(9, x, y, 'door_closedLock1.png', True)
           if block == "&":
                block = Blocks(10, x, y, 'door_closedLock2.png', True)
    

           if block != "-":
                block.rect.x = x
                block.rect.y = y
                x += 50
                allTypes.append(block)
                tile_x += 1 
                
           
           if block == "-":
                x += 50 
                tile_x += 1
                       
           
           if x == len(gotTypes.all_types[0])*50:
                y += 50
                x = 0
                tile_y += 1
                tile_x = 0

                


                
class Blocks(object):
    def __init__(self, ID, x, y, pic, wall):
        self.ID = ID
        self.is_wall = wall
        self.image = self.GetImage(pic)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.onScreen = True
        self.parent = (0,0)
        self.gx = 0
        self.hx = 0
        self.fx = self.gx + self.hx
        self.location = (self.rect.x / 50 ,self.rect.y / 50)
        self.tile_x = self.location[0]
        self.tile_y = self.location[1]
        self.drawnOver = False
        self.seen = False
       

    def GetImage(self, pic):
    
        self.pic = pic
        if not type(pic) is int: 
            img_file = os.path.join('img', self.pic)
            self.image = gb.pygame.image.load(img_file).convert()
            return self.image
                

def cycleBlock(selected, types):
    if types == "block":

        for loc, blocks in enumerate(all_block_types):
            if selected.ID == blocks.ID:
                whereIs = loc
                end = len(all_block_types) - 1
                if whereIs != end:
                    selected = all_block_types[whereIs + 1]
                
                
                if whereIs == end:
                    selected = all_block_types[0]
                    
                break    

    if types == "obj":
        for loc, obj in enumerate(gb.objects.all_object_types):
            if selected.ID == obj.ID:
                whereIs = loc
                end = len(gb.objects.all_object_types) - 1
                if whereIs != end:
                    selected = gb.objects.all_object_types[whereIs + 1]
                if whereIs == end:
                    selected = gb.objects.all_object_types[0]

                break
        
    return selected



def inherent(selected, x, y):
    block = Blocks(selected.ID, x, y,selected.pic, selected.is_wall)
    return block


def loadMap():
    global level
    level = AddBlockType() 
    RenderMap()
        

def unloadBlocks(new_blocks):
    i = 0 
    for blocks in new_blocks:
        
        stored = [blocks.ID, blocks.rect.x, blocks.rect.y,
            blocks.pic, blocks.is_wall]
        new_blocks[i] = stored 
        i += 1
    return new_blocks
        

def unloadObjects(objects):
    i = 0
    for obj in objects:
        stored = [obj.ID, obj.pic, obj.rect.x, obj.rect.y]
        objects[i] = stored
        i += 1

    return objects




def save():
    global new_blocks
    with open(os.getcwd() + '/saves/' + gb.mapName, 'w') as f:
        new_blocks = unloadBlocks(new_blocks)
        gb.objects.all_objects = unloadObjects(gb.objects.all_objects)
        charInfo = [gb.player.rect]
        if gb.objects.all_objects:
            for obj in gb.objects.all_objects:
                new_blocks.append(obj)

        new_blocks.append(charInfo)
        gb.pickle.dump(new_blocks, f)

        
        
        

def load():
    with open(os.getcwd() + '/saves/' + gb.mapName, 'r') as f:
        new_blocks = gb.pickle.load(f)
        objects = []
        i = 0        
        gb.player.rect = new_blocks[-1][0]
        new_blocks.remove(new_blocks[-1])
        
        for block in new_blocks:
            if block[0] > 99:
                
                block = gb.objects.Objects(block[0], 
                    block[1], block[2], block[3])
                objects.append(block)
                new_blocks[i] = block
                i += 1

            elif block[0] < 99:
                if block[0] == 2:
                    gb.player.rect.x, gb.player.rect.y = block[1], block[2]

                block = Blocks(block[0],block[1],block[2],block[3],block[4])
                new_blocks[i] = block
                i += 1
        
        for obj in objects:
            # SPIKES
            if obj.ID == 102: 
                obj.direction = "up"
            if obj.ID == 103:
                obj.direction = "left" 
            #TURRETS
            if obj.ID == 104: 
                obj.makeTurret()
                obj.direction = "left"
            if obj.ID == 105:
                obj.makeTurret()
                obj.direction = "right"
            if obj.ID == 106:
                obj.makeTurret()
                obj.direction = "up"           
            if obj.ID == 107:
                obj.makeTurret()
                obj.direction = "down"            
            
            if obj in new_blocks:
                new_blocks.remove(obj)

        return [new_blocks, gb.player.rect, objects]      
        

        

def getAdjacents(source, door):
    open = []
    for adjacent in source:
        for (i, j) in ADJACENTS:
            check = (adjacent.location[0]+i, adjacent.location[1]+j)
            for block in new_blocks:
                if check == block.location:
                    check = block

                    if door:
                        if not block.seen:
                            block.seen = True
                            open.append(check)


                    else:
                        if block.ID != 4:  
                            if not block.drawnOver:
                                block.drawnOver = True
                                if not block.is_wall:        
                                    open.append(check)
    
     
    return open



def render():
    for block in new_blocks:       
        
        if block in gb.player.sight or gb.player2.sight or gb.edit.editing:
            screenposX = (block.rect.x - gb.cam.rect.x) / 50
            screenposY = (block.rect.y - gb.cam.rect.y) / 50
            if screenposX > 800 / 50:
                block.onScreen = False
            elif screenposX < -50:
                block.onScreen = False
            elif screenposY > 800 / 50:
                block.onScreen = False
            elif screenposY < -50:
                block.onScreen = False
                
            else:
                block.onScreen = True


            if block.onScreen == True:                 
                
                gb.window.screen.blit(block.image,(block.rect.x - gb.cam.rect.x, 
                    block.rect.y - gb.cam.rect.y))    
         


    gb.objects.UpdateObjects()
    gb.projectiles.Render()    
             

ADJACENTS = ((1,0), (-1,0), (0,1), (0,-1), (1,1), (1, -1), (-1, 1), (-1, -1))    
lights = []
gotTypes = AddBlockType()       
allTypes = []
RenderMap()


