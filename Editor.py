import Globals as gb
class Editor():
    def __init__(self):
        self.editing = False
        self.draggingL = False
        self.draggingR = False
        self.selected = gb.maps.all_block_types[0]
        self.mouseHover = True
        self.mode = "blocks"
        self.pauseMoving = True
    def makeBlock(self, type):
        if type == "block":
            emptySpace = True
            posx, posy = gb.pygame.mouse.get_pos()
            posx += gb.cam.rect.x
            posy += gb.cam.rect.y
            roundX = int(50 * round(posx / 50))
            roundY = int(50 * round(posy / 50))
            newblock = gb.maps.inherent(self.selected, roundX, roundY)
            
            for block in gb.maps.new_blocks:
                if block.rect.collidepoint(posx, posy): 
                    gb.maps.new_blocks.remove(block)
                    gb.maps.new_blocks.append(newblock)
                    emptySpace = False
                    break
            if emptySpace:
                gb.maps.new_blocks.append(newblock)  
        
        
        
        elif type == "object":
            posx, posy = gb.pygame.mouse.get_pos()
            posx += gb.cam.rect.x
            posy += gb.cam.rect.y
            roundX = int(50 * round(posx / 50))
            roundY = int(50 * round(posy / 50))
            newobject = gb.objects.inherent(self.selected, roundX, roundY)
            gb.objects.all_objects.append(newobject)
            for block in gb.maps.new_blocks:
                if block.rect.collidepoint(posx, posy):
                    block.drawnOver = newobject           
    
    def RunEditor(self):
        
        
        
        if self.mode == "blocks":
            ev = gb.pygame.event.get()
            for e in ev:
                if e.type == gb.pygame.QUIT:
                    self.editing = False
                    
                if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_p:
                    self.pauseMoving = not self.pauseMoving
                    
                if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_h:
                    self.mouseHover = not self.mouseHover
               
                if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_c:
                    self.selected = gb.maps.cycleBlock(self.selected, "block")         
        
                if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_m:
                    self.mode = "obj"
                    self.selected = gb.objects.all_object_types[0]
                if e.type == gb.pygame.MOUSEBUTTONDOWN:
                    if e.button == 3:
                        self.draggingR = True
                        for block in gb.maps.new_blocks:
                            if block.rect.collidepoint(e.pos[0] + gb.cam.rect.x,
                                e.pos[1] + gb.cam.rect.y):
                                gb.maps.new_blocks.remove(block)
                    
                    if e.button == 1:                
                        self.makeBlock("block")
                        self.draggingL = True
                    
                    
                    if e.button == 2:
                        for block in gb.maps.new_blocks:
                            if block.rect.collidepoint(e.pos[0] + gb.cam.rect.x,
                                e.pos[1] + gb.cam.rect.y):
                                self.selected = block
                if e.type == gb.pygame.MOUSEBUTTONUP:
                    if e.button == 3:
                        self.draggingR = False
                    if e.button == 1:
                        self.draggingL = False
                if self.draggingR:
                    posx, posy = gb.pygame.mouse.get_pos()
                    
                    for block in gb.maps.new_blocks:
                        if block.rect.collidepoint(posx + gb.cam.rect.x,
                            posy + gb.cam.rect.y):
                            gb.maps.new_blocks.remove(block)
                if self.draggingL:
                    self.makeBlock("block")            
        
        else:
            
            ev = gb.pygame.event.get()
            for e in ev:
                if e.type == gb.pygame.QUIT:
                    self.editing = False
                    self.Saving()
                
                if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_p:
                    self.pauseMoving = not self.pauseMoving                
                
                if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_h:
                    self.mouseHover = not self.mouseHover
                if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_c:
                    self.selected = gb.maps.cycleBlock(self.selected, "obj") 
                if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_m:
                    self.mode = "blocks"
                    self.selected = gb.maps.all_block_types[0]
                if e.type == gb.pygame.MOUSEBUTTONDOWN:
                    if e.button == 3:
                        for obj in gb.objects.all_objects:
                            if obj.rect.collidepoint(e.pos[0] + gb.cam.rect.x,
                                e.pos[1] + gb.cam.rect.y):
                                gb.objects.all_objects.remove(obj)
                    if e.button == 2:
                        for obj in gb.objects.all_objects:
                            if obj.rect.collidepoint(e.pos[0] + gb.cam.rect.x,
                                e.pos[1] + gb.cam.rect.y):
                                self.selected = obj
                    if e.button == 1:
                        self.makeBlock("object")
                
                        
        
        
        
        
        
        
        gb.maps.render()
        if self.mouseHover:
            posx, posy = gb.pygame.mouse.get_pos()
            gb.window.screen.blit(self.selected.image, (posx - 25 , posy - 25))
            outLine = gb.pygame.draw.rect(gb.window.screen, (100, 200, 200),
                (posx - 25, posy - 25, 51, 51), 2)
        gb.pygame.display.flip()    
        gb.window.RenderWindow('black')    
 
        key = gb.pygame.key.get_pressed()
        
        if key[gb.pygame.K_a]:
            gb.cam.rect.x -= 3
        if key[gb.pygame.K_d]:
            gb.cam.rect.x += 3
        if key[gb.pygame.K_s]:
            gb.cam.rect.y += 3
        if key[gb.pygame.K_w]:
            gb.cam.rect.y -= 3
        if key[gb.pygame.K_ESCAPE]:
            self.Saving()
    def Saving(self):
        waiting = True
        key = gb.pygame.key.get_pressed()
        gb.pygame.font.init()
        myfont = gb.pygame.font.SysFont("monospace", 30)
        color = (0,0,0)
        while waiting:
            event = gb.pygame.event.poll()
            if event.type == gb.pygame.QUIT:
                waiting = False
            gb.maps.render()
            
            saveText = myfont.render("Save", 1, (255, 255, 255))
            quitText = myfont.render("Quit", 1, (255, 255, 255))
            
           
            yesBox = gb.pygame.draw.rect(gb.window.screen, (color), 
                (((800/3)), 100, 125, 50))  
            noBox = gb.pygame.draw.rect(gb.window.screen, (color), 
                ((((800/4)*2)), 100, 125, 50))
            
            yesOutline = gb.pygame.draw.rect(gb.window.screen, (255,100,100), 
                (yesBox.x, yesBox.y, 125, 50), 2)
            noOutline = gb.pygame.draw.rect(gb.window.screen, (255,100,100), 
                (noBox.x, noBox.y, 125, 50), 2)
            
            posx, posy = gb.pygame.mouse.get_pos() 
            if event.type == gb.pygame.KEYDOWN and event.key == gb.pygame.K_ESCAPE:
                waiting = False
                 
            if event.type == gb.pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if yesBox.collidepoint(posx, posy):
                        gb.maps.save()
                        gb.LoadGame()
                        waiting = False
                    if noBox.collidepoint(posx, posy):
                        waiting = False
                        gb.playing = False
                        gb.SettingUp.SetUp(True)
            
            gb.window.screen.blit(saveText, (yesBox.x + 30, yesBox.y + 10))
            gb.window.screen.blit(quitText, (noBox.x + 30, noBox.y + 10))
           
            gb.pygame.display.flip()
            gb.window.RenderWindow('black')
            
  
        
