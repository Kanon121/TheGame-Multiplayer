import Globals as gb
class Associate():
    def __init__(self, text, id, offset, saves):
        self.surface = text
        self.rect = gb.pygame.Surface.get_rect(self.surface)
        self.ID = id
        self.rect.x = 30
        self.rect.y = 10 + offset
        GetID(self, saves)

def GetID(text, saves):
    text.ID = saves[text.ID]

def SetUp(settingUp):        

    if settingUp:

        typed = []
        files = []
        saves = []
        files.append(gb.os.listdir(gb.os.getcwd() + "/saves/"))
        checked = 0
        displayGames = []
        gb.pygame.font.init()
        myfont = gb.pygame.font.SysFont("monospace", 30)
        

        
        files = [file for sublist in files for file in sublist]
        for file in files:
            #if file[-10:] == ".custommap":
            if file[-6:] == ".level":
                saves.append(file)

        for save in saves:
            displayGames.append(myfont.render(str(save), 1, (255, 255, 255)))

        while settingUp:
            offset = 0
            id = 0
            event = gb.pygame.event.poll()
            
            for text in displayGames:
                
                text = Associate(text, id, offset, saves)
                id += 1
                offset += 30
                if event.type == gb.pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if text.rect.collidepoint(gb.pygame.mouse.get_pos()):
                            settingUp = False
                            gb.maps.save()
                            gb.mapName = text.ID
                            gb.LoadGame()   
                            



            offset = 0
            for text in displayGames:    
                gb.window.screen.blit(text, (30, 10 + offset))
                offset += 30

            if event.type == gb.pygame.QUIT:
                settingUp = False
                exit()
               # keyHit = chr(event.key)
     

            gb.pygame.display.flip()
            gb.window.RenderWindow('black')
SetUp(True)
