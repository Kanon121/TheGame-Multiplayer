from PodSixNet.Channel import Channel
from PodSixNet.Server import Server
from time import sleep
import os
import pygame


class ClientChannel(Channel):
    def __init__(self, *args, **kwargs):
        Channel.__init__(self, *args, **kwargs)

    def Network(self, data):
        print data

    def Network_Move(self, data):
        direction = data['direction']
        if data['num'] == 0:
            self._server.Move(0, direction)
        else:
            self._server.Move(1, direction)


class GameServer(Server):
    channelClass = ClientChannel
	
    def __init__(self, *args, **kwargs):
        Server.__init__(self, *args, **kwargs)    
        self.queue = None
        self.currentIndex = 0
        self.game = None
    
    def Connected(self, channel, addr):
        print "new connection: ", channel
        if self.queue == None:
            self.currentIndex += 1
            self.queue = Game(channel, self.currentIndex)
        else:
            self.queue.player1 = channel
            self.queue.player0.Send({'action': 'startgame', 'player': 0, 'gameid':0})
            self.queue.player1.Send({'action': 'startgame', 'player': 1, 'gameid':1})
            self.game = self.queue
            self.queue = None
 
    def Move(self, num, dir):
        self.game.Move(num, dir)
    




 
 
 
 
 
class Game():
    def __init__(self, player0, currentIndex):
        self.player0 = player0
        self.player1 = None
        self.currentIndex = currentIndex


    def Move(self, num, dir):
        self.player0.Send({'action': 'movePlayer', 'num': num, 'direction': dir })
        self.player1.Send({'action': 'movePlayer', 'num': num, 'direction': dir })      
        

print "STARTING SERVER ON LOCALHOST"

mainServer = GameServer()

while True:
    mainServer.Pump()
    sleep(0.01)
    
    
    
    
    