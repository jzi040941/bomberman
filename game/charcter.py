import pygame, sys
from pygame.locals import *

sys.path.append("C:/Python32/bomberman/game")

import settings
from settings import *

import time, math, random

import charcter, game_system, screen, map_system, bomb

from charcter import *
from game_system import *
from screen import *
from map_system import *
from bomb import *

import threading

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

#캐릭터 클래스
class character :
    playmap=None
    chartype=None
    player=0
    
    global CharImg_L, CharImg_R, UP, DOWN, LEFT, RIGHT
    CharImg_L = pygame.image.load('C:/Python32/bomberman/sprite/guard_0.png')
    CharImg_R = pygame.transform.flip(CharImg_L,True,False)
    

       
    #이동관련
    # 위, 아래, 왼쪽 오른쪽 #키보드 입력
    ableMove = [False, False, False, False]#맵상에서 캐릭터가 움직일수 있는 곳
    centerSignal = True #교차
    
    #isValidMove=None
    speed=0

    #폭탄
    
    bombrange=0
    

    #캐릭터 그래픽 표시 관련
    surface=None
    rect=None

    #현재위치한 타일 좌표
    tileX,tileY=1,7
    char_x,char_y=0,0
    
    def __init__(self,playmap,chartype,player) :
        self.playmap=playmap
        self.chartype=chartype
        self.player=player
        self.moveSignal = [False, False, False, False]
        #self.char_x,self.char_y=givexy(playmap)
        self.char_x,self.char_y=getLeftTopOfBlock(self.tileX, self.tileY)#임시로 맵 왼쪽위 받아옴
        #self.isValidMove=True
        self.speed=3
        self.bombnum=1
        self.bombrange=1
        self.surface = pygame.transform.scale(CharImg_L, CHARSIZE)

        self.bombs=[]
        
        if (self.chartype=='A') : # 추후에 이름 수정
            self.speed+=1
        elif (self.chartype=='B') :
            self.bombnum+=1
        else :
            self.bombrange+=1

        self.ablebombnum=self.bombnum
        
    def move(self, board) :
        if self.moveSignal[LEFT] and self.isValidMove(LEFT, board) :
            #self.char_x-=self.speed
            self.centerCheck(-self.speed,0)
            self.checkAndChangeTile(self.tileX-1, self.tileY)
        if self.moveSignal[RIGHT] and self.isValidMove(RIGHT, board) :
            #self.char_x+=self.speed
            self.centerCheck(+self.speed,0)
            self.checkAndChangeTile(self.tileX+1, self.tileY)
        if self.moveSignal[UP] and self.isValidMove(UP, board) :
            #self.char_y-=self.speed
            self.centerCheck(-self.speed,1)
            self.checkAndChangeTile(self.tileX, self.tileY-1)
        if self.moveSignal[DOWN] and self.isValidMove(DOWN, board) :
            #self.char_y+=self.speed
            self.centerCheck(+self.speed,1)
            self.checkAndChangeTile(self.tileX, self.tileY+1)

    # 움직일수 있는지 확인 후 움직일 수 없으면 False 움직일 수 있으면 True
    # 맵밖 벗어나지 않게 구현됨
    # 벽과 충돌 구현 필요

    
    def centerCheck(self,speed,xy):
        #xy if 0 -> x 1 -> y
        if(self.ableMove[UP] or self.ableMove[DOWN])and(self.ableMove[LEFT] or self.ableMove[RIGHT]):
            charCenter = int(self.rect.center[xy])
            tileCenter = int(getTileRect(self.tileX,self.tileY).center[xy])
            if(speed>0):
                if charCenter<tileCenter and tileCenter<charCenter+speed :
                    #self.rect.center = getTileRect(self.tileX,self.tileY).center
                    #print("here is center")
                    self.char_x,self.char_y = getLeftTopOfBlock(self.tileX, self.tileY)
                    self.centerSignal = False
                else:
                    self.charXYAddSpeed(xy, speed)
                    #print(xy)
                    self.centerSignal = True
            else:
                if(charCenter+speed<tileCenter and tileCenter<charCenter) :
                    #self.rect.center = getTileRect(self.tileX,self.tileY).center
                    self.char_x,self.char_y = getLeftTopOfBlock(self.tileX, self.tileY)
                    self.centerSignal = False
                else:
                    self.charXYAddSpeed(xy, speed)
                    #print(xy)
                    self.centerSignal = True
        else:
            self.charXYAddSpeed(xy, speed)

    def charXYAddSpeed(self, xy, speed):
        if xy == 0:
            self.char_x += speed
        else:
            self.char_y += speed
            
    def isValidMove(self, move, board):
        '''
wd        return (move == DOWN and self.tileY != BOARDHEIGHT - 1) and board[self.tileX][self.tileY+1] == 0 or \
           (move == UP and self.tileY != 0 and board[self.tileX][self.tileY-1] == 0)  or \
           (move == LEFT and self.tileX != 0 and board[self.tileX-1][self.tileY] == 0)  or \
           (move == RIGHT and self.tileX != BOARDWIDTH - 1 and board[self.tileX+1][self.tileY] == 0)
        '''
        self.ableMove[UP]=self.tileY != 0 and board[self.tileX][self.tileY-1] == 0
        self.ableMove[DOWN]=self.tileY != BOARDHEIGHT - 1 and board[self.tileX][self.tileY+1] == 0
        self.ableMove[RIGHT]=self.tileX != BOARDWIDTH - 1 and board[self.tileX+1][self.tileY] == 0
        self.ableMove[LEFT]=self.tileX != 0 and board[self.tileX-1][self.tileY] == 0
        if move == DOWN:
            #if self.rect.center[0]!=getTileRect(self.tileX,self.tileY).center[0]:
            if self.char_x != getLeftTopOfBlock(self.tileX, self.tileY)[0]:
                return False
            if self.ableMove[move]:
                return True
            else:
                if(self.rect.center[1]<getTileRect(self.tileX,self.tileY).center[1]):
                    return True
                else:
                    #self.rect.center=getTileRect(self.tileX,self.tileY).center
                    return False
        elif move == UP:
            #if self.rect.center[0]!=getTileRect(self.tileX,self.tileY).center[0]:
            if self.char_x != getLeftTopOfBlock(self.tileX, self.tileY)[0]:
                return False
            if self.ableMove[move]:
                return True
            else:
                if(self.rect.center[1]>getTileRect(self.tileX,self.tileY).center[1]):
                    return True
                else:
                    #self.rect.center=getTileRect(self.tileX,self.tileY).center
                    return False
                
        elif move == RIGHT:
            #if self.rect.center[1]!=getTileRect(self.tileX,self.tileY).center[1]:
            if self.char_y != getLeftTopOfBlock(self.tileX, self.tileY)[1]:
                return False
            if self.ableMove[move]:
                return True
            else:
                if(self.rect.center[0]<getTileRect(self.tileX,self.tileY).center[0]):
                    return True
                else:
                    #self.rect.center=getTileRect(self.tileX,self.tileY).center
                    return False
        elif move == LEFT:
            #if self.rect.center[1]!=getTileRect(self.tileX,self.tileY).center[1]:
            if self.char_y != getLeftTopOfBlock(self.tileX, self.tileY)[1]:
                return False
            if self.ableMove[move]:
                return True
            else:
                if(self.rect.center[0]>getTileRect(self.tileX,self.tileY).center[0]):
                    return True
                else:
                    #self.rect.center=getTileRect(self.tileX,self.tileY).center
                    return False
            
    def showchar(self, surf) :
        #DISPLAYSURF.blit(CharImg_l,(self.char_x,self.chaar_y))
        self.rect = pygame.Rect( (self.char_x,
                                              self.char_y, 
                                              TILESIZE,
                                              TILESIZE) )
        surf.blit(self.surface,self.rect)

    #캐릭터의 픽셀좌표를 이용해 방향에 따라 확인 후 
    def checkAndChangeTile(self, newTileX, newTileY):
        left, top = getLeftTopOfBlock(newTileX, newTileY)
        tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE)
        if tileRect.collidepoint(self.rect.center[0], self.rect.center[1]):
        #if tileRect.collidepoint(self.char_x, self.char_y):
            self.tileX,self.tileY = newTileX,newTileY

    
    def setMoveSignal(self, direction, signal):
        self.moveSignal[direction] = signal

    def setSpeed(self, speed):
        self.speed = speed

    def putbomb(self,surf,player) :
        if self.ablebombnum!=0 :
            a=bomb(surf,player)
            (self.bombs).append(a)
            self.ablebombnum-=1


def getTileRect(tileX,tileY):
    left, top = getLeftTopOfBlock(tileX, tileY)
    tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE)
    return tileRect


