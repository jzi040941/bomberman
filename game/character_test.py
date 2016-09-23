import pygame, sys
from pygame.locals import *

sys.path.append("C:/Python32/bomberman/game")

import settings
from settings import *

import time, math, random

import charcter, game_system, screen, map_system
from charcter import *
from game_system import *
from screen import *
from map_system import *

import threading

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

class character :
     
    def __init__(self, pos, player) :

        #charProperty
        self.speed = 3

        #bomb
        self.bombs=[]
        self.bombNum = 1
        self.bombRange = 1
        self.ablebombnumb = 1
        self.ablebombnum = 1

        #move
        self.posX = pos[0]
        self.posY = pos[1]
        self.moveValid = [True, True, True, True]

        self.moveleft = False
        self.moveright = False
        self.moveup = False
        self.movedown = False

        #charRect
        self.CharImg = pygame.image.load('C:/Python32/bomberman/sprite/guard_0.png')
        self.surface = pygame.transform.scale(self.CharImg, CHARSIZE)
        self.rect = pygame.Rect(self.posX, self.posY, CHARSIZE[0], CHARSIZE[1])
                 
    def move(self) :
        if self.posX<0:
            self.moveValid[LEFT] = False
        if self.posX>WINDOWWIDTH:
            self.moveValid[RIGHT] = False
        if self.posY<0:
            self.moveValid[UP] = False
        if self.posX>WINDOWHEIGHT:
            self.moveValid[DOWN] = False
            
        if self.moveup  and self.moveValid[UP] :
            self.posY -= self.speed
        if self.movedown and self.moveValid[DOWN] :
            self.posY +=self.speed
        if self.moveleft and self.moveValid[LEFT] :
            self.posX -= self.speed
        if self.moveright and self.moveValid[RIGHT] :
            self.posX += self.speed
                
    def addSpeed(self, accel):
        self.speed += accel

    def collideCheck(self, Obj):        
        if self.moveleft and self.rect.colliderect(Obj):
            self.moveValid[LEFT] = False
        if self.moveright and self.rect.colliderect(Obj):
            self.moveValid[RIGHT] = False
        if self.moveup and self.rect.colliderect(Obj):
            self.moveValid[UP] = False
        if self.movedown and self.rect.colliderect(Obj):
            self.moveValid[DOWN] = False

    def blockCheck(self):
        pass

    def animation(self):
        pass   
            
    def showChar(self, surf) :
        self.rect = pygame.Rect(self.posX, self.posY, CHARSIZE[0], CHARSIZE[1])
        surf.blit(self.surface, self.rect)

    def putbomb(self, surf, player) :
        if self.ablebombnum!=0 :
            a=bomb(surf,player)
            (self.bombs).append(a)
            self.ablebombnum-=1

class bomb :
    collideSignal = False
    #loc_x,loc_y=0,0
    bombimage=pygame.image.load('C:/Python32/bomberman/sprite/bombimage.png')
    bombimage=pygame.transform.scale(bombimage,(TILESIZE,TILESIZE))

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
        
    def show(self,surf,players) :
        if self.timeCheck(time.time(),self.exploseTime) :
            surf.blit(self.bombimage,self.bombimagerect)
        elif self.timeCheck(time.time(),self.endTime) :
            for position in self.bombSurround :
                self.bombRectBatch.append(pygame.draw.rect(surf, RED, (position[0],position[1],SIZE(BLOCK),SIZE(BLOCK))))
                self.collideCheck(self.bombRectBatch, players)
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
        '''
        if self.tileX>1 :
            bombSurround.append(pygame.Rect(getLeftTopOfBlock(self.tileX-1, self.tileY),
                                            (SIZE(BLOCK),SIZE(BLOCK)))
        
        if self.tileX<BOARDWIDTH :
            bombSurround.append(pygame.Rect(getLeftTopOfBlock(self.tileX+1, self.tileY),
                                            (SIZE(BLOCK),SIZE(BLOCK)))
        if self.tileY>1 :
            bombSurround.append(pygame.Rect(getLeftTopOfBlock(self.tileX, self.tileY-1),
                                            (SIZE(BLOCK),SIZE(BLOCK)))
        if self.tileY<BOARDHEIGHT :
            bombSurround.append(pygame.Rect(getLeftTopOfBlock(self.tileX, self.tileY+1),
                                            (SIZE(BLOCK),SIZE(BLOCK)))
        bombSurround.append(pygame.Rect((self.loc_x,self.loc_y),
                                            (SIZE(BLOCK),SIZE(BLOCK)))
        '''
        return bombSurround
    def animation(self, bombSurround, surf):
            pygame.draw.rect(surf, RED, (position[0],position[1],BLOCKSIZE,BLOCKSIZE))
