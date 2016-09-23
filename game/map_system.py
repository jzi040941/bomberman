import pygame, sys
from pygame.locals import*

sys.path.append("C:/Python32/bomberman/game")
import settings
from settings import*
#NAME
NORMAL = 'normal'
BLANK = 'blank'

blockIMG = pygame.image.load('C:/Python32/bomberman/sprite/tree.png')
blockSurf = pygame.transform.scale(blockIMG, (BLOCKSIZE, BLOCKSIZE))

    
def generateBoard():
    board = []
    for boardx in range(BOARDWIDTH):
        column = []
        for boardy in range(BOARDHEIGHT):
            column.append(0)
        board.append(column)
    return board

def getLeftTopOfBlock(blockx, blocky):
    left = XMARGIN + (blockx * BLOCKSIZE) + (blockx - 1)
    top = YMARGIN + (blocky * BLOCKSIZE) + (blocky - 1)
    return (left, top)

def drawText(surf, font, message, color, textx, texty ):
    textSurf = font.render('%s' %messgae, True, color, 0)
    testRect = textSurf.get_rect(center = (textx, texty))
    surf.blit(textSurf, textRect)


def drawBlock(surf, type, blockx, blocky):
       
    """block type:

    normal
    
    """

    posx, posy = getLeftTopOfBlock(blockx, blocky)
    
    if type == NORMAL:
        blockRect = pygame.draw.rect(surf, BGCOLOR, (posx, posy, BLOCKSIZE, BLOCKSIZE), 1)
        surf.blit(blockSurf, blockRect)

    if type == BLANK:
        blockRect = Rect(posx, posy, BLOCKSIZE, BLOCKSIZE)
        
    else:
        pass
    

def displayBoard(surf, board):
    surf.fill(BGCOLOR)
    for blockx in range(BOARDWIDTH):
        for blocky in range(BOARDHEIGHT):
            if board[blockx][blocky] == 1:
                drawBlock(surf, NORMAL, blockx, blocky )
            elif board[blockx][blocky] == 0:
                drawBlock(surf, BLANK, blockx, blocky )

#set__Position surf 안받게 변경
def setBlankPosition(board, blockx, blocky):
    board[blockx][blocky] = 0
    
def setNormalPosition(board, blockx, blocky):
    board[blockx][blocky] = 1

def makeBlankTileSet(blankSet, board):
    for blockx in range(BOARDWIDTH):
        for blocky in range(BOARDHEIGHT):
            if(board[blockx][blocky] == 0):
                blankSet.add((blockx,blocky))

def normalList(board):
    normalList = []
    for blockx in range(BOARDWIDTH):
        for blocky in range(BOARDHEIGHT):
            if board[blockx][blocky] == 1:
                posx, posy = getLeftTopOfBlock(blockx, blocky)
                normalList.append(Rect(posx, posy, BLOCKSIZE, BLOCKSIZE))
            else:
                pass
                                  
    return normalList
