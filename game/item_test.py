import pygame, sys
from pygame.locals import *

sys.path.append("C:/Python32/bomberman/game")

import settings, random, threading
from settings import *
from game_system import *
from screen import *
from map_system import *


maxItemNum = 1


def addItem(itemObjs,time,blankTileSet,displaysurf):
    for i in range(0,random.randint(1,3)):
        itemObjs.append(item(time,blankTileSet,displaysurf,random.randint(0,1)))

class item:
    
    #ITEM_IMG = pygame.image.load('C:/Python32/bomberman/sprite/item.png')
    ITEMIMG = []
    for i in range(0, maxItemNum+1):
        ITEMIMG.append(pygame.image.load('C:/Python32/bomberman/sprite/item%s.png' % i))
        
    def __init__(self,time,blankTileSet,displaysurf,item_num):
       
        randomBlankTile = blankTileSet.pop()
        self.item_num = item_num
        self.surface =  pygame.transform.scale(self.ITEMIMG[item_num], (TILESIZE, TILESIZE))
        self.tileX = randomBlankTile[0]
        self.tileY = randomBlankTile[1]
        self.delTimer = threading.Timer(time/2,self.delSignalOn)
        self.delTimer.start()
        self.delSignal = False
        self.drawItem(displaysurf)
        
    def delSignalOn(self):
        self.delSignal = True
        
    def drawItem(self,displaysurf):
        self.itemLeftTop = getLeftTopOfBlock(self.tileX, self.tileY)
        self.rect = pygame.Rect( (self.itemLeftTop[0],self.itemLeftTop[1],
                                                  TILESIZE,
                                                  TILESIZE) )
        displaysurf.blit(self.surface, self.rect)

    def checkAndDraw(self, players):
        self.checkCollidePlayerAndEvent(players[0])
        self.checkCollidePlayerAndEvent(players[1])

    def checkCollidePlayerAndEvent(self, player):
        if self.rect.collidepoint(player.rect.center):
            
            #충돌한 플레이어에게 발동할 이벤트 (속도증가 등등)
            #ex) 속도증가
            if self.item_num == 1:
                player.addSpeed(player.speed+3)
            elif self.item_num == 0:
                player.ablebombnum += 1
            self.delSignalOn()
