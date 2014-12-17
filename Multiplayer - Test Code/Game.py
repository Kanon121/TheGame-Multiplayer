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

            
        else:
            print "Player 1!"


    def update(self):
        connection.Pump()
        self.Pump() 
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                connector.running = False
            
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                connector.running = False
        
            if e.type == pygame.KEYDOWN and e.key == pygame.K_m:
                self.Send({'action': 'Move', 'num': self.num, 'direction': "m"})
        

        
        
        
        pygame.display.flip()
        window.RenderWindow("black")
      
   
    
    
    def Network_movePlayer(self, data):
        if data['num'] == 0:
            print "0 moving"
            
        if data['num'] == 1:
            print "1 moving"
            
    
    
    
    
    def Network(self, data):
        #print data
        pass
    
    def Network_startgame(self, data):
        print "Starting!"
        self.running = True
        self.num = data["player"]
        self.gameid = data["gameid"]

    
window = Window()
screen_width = 800
screen_height = 800
pygame.init()
window.CreateWindow(screen_height, screen_width)
pygame.display.init()
        

connector = Connector()    

      
        
while connector.running:
    connector.update()
    





