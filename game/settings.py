#settings

import pygame, sys
from pygame.locals import *

sys.path.append("C:/Python32/bomberman/game")

BOARDWIDTH = 24  # number of columns in the board
BOARDHEIGHT = 13 # number of rows in the board

BLOCKSIZE = 50
TILESIZE = BLOCKSIZE
WINDOWWIDTH = 1280
WINDOWHEIGHT = 720
HALF_WINWIDTH = int(WINDOWWIDTH / 2)
HALF_WINHEIGHT = int(WINDOWHEIGHT / 2)
FPS = 60

#                 R    G    B
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
BRIGHTBLUE =    (  0,  50, 255)
DARKTURQUOISE = (  3,  54,  73)
GREEN =         (  0, 204,   0)
RED   =         (255,   0,   0)
BLUE  =         (  0,   0, 255)
GRAY  =         (100, 100, 100)
DGRAY =         ( 51,  51,  51)
LBGRN =         ( 54, 220, 184)

BGCOLOR = LBGRN
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BOARDCOLOR = BRIGHTBLUE
SCREENCOLOR = BLACK
BLOCKCOLOR = GRAY
BASICFONTSIZE = 20

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)
CHARSIZE = (int(BLOCKSIZE*1), int(BLOCKSIZE *1))

MAXHEALTH = 3
MOVERATE = 5         # how fast the player moves
