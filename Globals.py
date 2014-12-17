import pygame 
from Window import Window
import sys
import os
import random

playing = True
editing = False
reloadGame = False
try: 
    arg = sys.argv[1]
    if arg == "-edit":
        editing = True
        playing = False

    if arg == "-reload":
        reloadGame = True
except IndexError:
    pass

import pickle 
import copy

window = Window()
screen_width = 800
screen_height = 800
pygame.init()
window.CreateWindow(screen_height, screen_width)
pygame.display.init()



from Entity import Entity
from Camera import Camera
import Map as maps
import Objects as objects
from Overlay import Overlay
import Projectile as projectiles
overlay = Overlay()


cam = Camera(0, 0, screen_width, screen_height)

player = Entity(0, 0, 'guy2.png')
player2 = Entity(60, 60, 'guy2.png')

conjoinedSight = []

mapName = "level1.level"
onLevel = 1
def LoadGame():
    if not reloadGame:
        loadHolder = maps.load() 
        maps.new_blocks = loadHolder[0]
        player.rect = loadHolder[1]
        objects.all_objects = loadHolder[2]
    else:
        maps.loadMap()

LoadGame()
def MovePlayer():
    for block in maps.new_blocks:
        
        if block.ID == 2:
            
            start = block.rect.x, block.rect.y

    
    player.rect.x, player.rect.y = start
    player2.rect.x, player2.rect.y = start
    

if not reloadGame:
    MovePlayer()

maps.all_block_types = maps.allTypes


from Editor import Editor
edit = Editor()
if editing == True:
    edit.editing = True



clock = pygame.time.Clock()

entities = []

import SettingUp

