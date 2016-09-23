import pygame, sys
from pygame.locals import *

sys.path.append("C:/Python32/bomberman/game")

import settings
from settings import *

import game_system, map_system, time
from game_system import *
from map_system import *
explosion_image = []

def getsprite_from_image(sp, image,xdiv,ydiv):
    width,height=image.get_size()
    for j in range(0,ydiv,1):
        for i in range(0,xdiv,1):
            temp = image.subsurface((width/xdiv*i,height/ydiv*j,width/xdiv,height/ydiv))
            #temp = image.subsurface((width/xdiv*i,height/ydiv*j,width/xdiv,height/ydiv))
            appendimage=pygame.transform.scale(temp,(TILESIZE, TILESIZE))
            sp.append(appendimage)

class bomb :
    collideSignal = False
    #loc_x,loc_y=0,0
    bombimage=pygame.image.load('C:/Python32/bomberman/sprite/bombimage.png')
    bombimage=pygame.transform.scale(bombimage,(TILESIZE, TILESIZE))
    spritesheet = pygame.image.load('C:/Python32/bomberman/sprite/explosion_sprite.png')
    explosion_image = getsprite_from_image(explosion_image,spritesheet,5,5)
    

    exploseTime = 4
    endTime = 5
    
    def __init__(self,surf,player) :
        self.tileX, self.tileY = player.tileX, player.tileY
        self.bombimagerect=self.bombimage.get_rect()
        self.loc_x,self.loc_y=getLeftTopOfBlock(self.tileX, self.tileY)
        (self.bombimagerect).topleft=self.loc_x,self.loc_y
        self.bombtimer=time.time()
        self.bombSurround = self.makeBombSurroundPosition()
        self.bombRectBatch=[]
        self.ani_num = 0
    def show(self,surf,players) :
        if self.timeCheck(time.time(),self.exploseTime) :
            surf.blit(self.bombimage,self.bombimagerect)
        #elif self.timeCheck(time.time(),self.endTime) :
        elif self.ani_num<25:
            for position in self.bombSurround :
                self.animation(position,surf)
                self.collideCheck(self.bombRectBatch, players)
            self.ani_num+=1
    def collideCheck(self, bombRectBatch, players) :
        for player in players:
            for bombRect in bombRectBatch:
                self.collideSignal = self.collideSignal or bombRect.collidepoint(player.rect.center)
               
            
    def timeCheck(self,t,checkTime) :
        return t-self.bombtimer<checkTime
    def end(self, player) :
        player.ablebombnum+=1
    def makeBombSurroundPosition(self) :
        bombSurround = []

        #modify tileX,Y>1 -> 0
        #modify BOARDWIDTH,BOARDHEIGHT -> BOARDWIDTH,BOARDHEIGHT-1
        if self.tileX>0 :
            bombSurround.append(getLeftTopOfBlock(self.tileX-1, self.tileY))
        if self.tileX<BOARDWIDTH-1 :
            bombSurround.append(getLeftTopOfBlock(self.tileX+1, self.tileY))
        if self.tileY>0 :
            bombSurround.append(getLeftTopOfBlock(self.tileX, self.tileY-1))
        if self.tileY<BOARDHEIGHT-1 :
            bombSurround.append(getLeftTopOfBlock(self.tileX, self.tileY+1))
        bombSurround.append((self.loc_x,self.loc_y))
        return bombSurround
    def animation(self,position, surf):
        
        #self.bombRectBatch.append(pygame.draw.rect(surf, RED, (position[0],position[1], BLOCKSIZE, BLOCKSIZE)))
        #pygame.draw.rect(surf, RED, (position[0],position[1],BLOCKSIZE,BLOCKSIZE))
        exploseimagerect=self.bombimage.get_rect()
        exploseimagerect.topleft=position
        surf.blit(explosion_image[self.ani_num],exploseimagerect)
        self.bombRectBatch.append(exploseimagerect)


    
