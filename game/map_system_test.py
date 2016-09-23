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

class game_map:
    def __init__(self):
        pass
    
    def generateBoard(self):
        board = []
        for boardx in range(BOARDWIDTH):
            column = []
            for boardy in range(BOARDHEIGHT):
                column.append(0)
            board.append(column)
        return board

    def getLeftTopOfBlock(self, blockx, blocky):
        left = XMARGIN + (blockx * BLOCKSIZE) + (blockx - 1)
        top = YMARGIN + (blocky * BLOCKSIZE) + (blocky - 1)
        return (left, top)

    def drawText(self, surf, font, message, color, textx, texty ):
        textSurf = font.render('%s' %messgae, True, color, 0)
        testRect = textSurf.get_rect(center = (textx, texty))
        surf.blit(textSurf, textRect)

    def drawBlock(self, surf, type, blockx, blocky):
        posx, posy = self.getLeftTopOfBlock(blockx, blocky)
        
        if type == NORMAL:
            blockRect = pygame.draw.rect(surf, BGCOLOR, (posx, posy, BLOCKSIZE, BLOCKSIZE), 1)
            surf.blit(blockSurf, blockRect)

        if type == BLANK:
            blockRect = Rect(posx, posy, BLOCKSIZE, BLOCKSIZE)
            
        else:
            pass

    def displayBoard(self, surf, board):
        for blockx in range(BOARDWIDTH):
            for blocky in range(BOARDHEIGHT):
                if board[blockx][blocky] == 1:
                    self.drawBlock(surf, NORMAL, blockx, blocky )
                elif board[blockx][blocky] == 0:
                    self.drawBlock(surf, BLANK, blockx, blocky )

    def setBlankPosition(self, board, pos):
        pos[0] = blockx
        pos[1] = blocky
        board[blockx][blocky] = 0
        
    def setNormalPosition(self, board, pos):
        pos[0] = blockx
        pos[1] = blocky
        board[blockx][blocky] = 1

    def makeBlankTileSet(self, blankSet, board):
        for blockx in range(BOARDWIDTH):
            for blocky in range(BOARDHEIGHT):
                if(board[blockx][blocky] == 0):
                    blankSet.add((blockx,blocky))

