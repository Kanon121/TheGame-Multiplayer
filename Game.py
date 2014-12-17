import pygame
import os
from Window import Window
from PodSixNet.Connection import ConnectionListener, connection
from time import sleep



class Connector(ConnectionListener):
    
    def __init__(self):
        self.Connect()
        self.running = False

        
        
        while not self.running:
            connection.Pump()
            self.Pump()          
            sleep(0.01)
        if self.num == 0:
            print "Player 0!"
            self.player0 = True
            self.player1 = False


        else:
            print "Player 1!"
            self.player1 = True
            self.player0 = False



    def update(self):
        connection.Pump()
        self.Pump() 

        
        time_passed = gb.clock.tick(60)
        for e in gb.pygame.event.get():
            if e.type == gb.pygame.QUIT:
                connector.running = False
                
            if e.type == gb.pygame.KEYDOWN and e.key == gb.pygame.K_ESCAPE:
                connector.running = False
                
        key = gb.pygame.key.get_pressed()

        if key[gb.pygame.K_a]:
            self.Send({'action': 'Move', 'num': self.num, 'direction': "left"})    
        if key[gb.pygame.K_d]:
            self.Send({'action': 'Move', 'num': self.num, 'direction': "right"})
        if key[gb.pygame.K_s]:
            self.Send({'action': 'Move', 'num': self.num, 'direction': "down"})
        if key[gb.pygame.K_w]:
            self.Send({'action': 'Move', 'num': self.num, 'direction': "up"})

                
                
                
        gb.maps.render()    

        
        if self.player0:
            gb.cam.update(False, gb.player)
        else:
            gb.cam.update(False, gb.player2)
        
        for ents in gb.entities:
            ents.render(gb.cam)
            ents.see()
         
        
        gb.player.render(gb.cam)
        gb.player2.render(gb.cam)
      
        gb.player.see(gb.maps.new_blocks)
        
        gb.player2.see(gb.maps.new_blocks)


        
        gb.projectiles.Update()
        
        gb.overlay.render()
        

        gb.pygame.display.flip()
        gb.window.RenderWindow('black')
          
   
    
    
    
    
    def Network(self, data):
        #print data
        pass
    
    def Network_startgame(self, data):
        print "Starting!"
        self.running = True
        self.num = data["player"]
        self.gameid = data["gameid"]

    def Network_movePlayer(self, data):
        if data['num'] == 0:
            player = gb.player
            
        if data['num'] == 1:
            player = gb.player2
        
        if data['direction'] == "up":
            player.update("up")
        if data['direction'] == "down":
            player.update("down")
        if data['direction'] == "left":
            player.update("left")
        if data['direction'] == "right":
            player.update("right")

connector = Connector()    

import Globals as gb      

while connector.running:
    connector.update()
    





