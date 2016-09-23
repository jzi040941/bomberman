import pygame, sys
from pygame.locals import*

sys.path.append("C:/Python32/bomberman/game")

import map_system_test
from map_system_test import*

def main():
    global DISPLAYSURF, FPSCLOCK, editedMap
    
    pygame.init()
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('mapEditor')
    
    #initMap
    editedMap = game_map()
    mainBoard = editedMap.generateBoard()

    editing = True

    f = open("C:/Python32/bomberman/game/maps/mapData.txt", 'a')
    
    while editing:
        DISPLAYSURF.fill(BGCOLOR)
        editedMap.displayBoard(DISPLAYSURF, mainBoard)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                spotx, spoty = getSpotClicked(event.pos[0], event.pos[1])

                if (spotx, spoty) == (None, None):
                    pass
                
                else:
                    if mainBoard[spotx][spoty] == 1:
                        pass
                    else:
                       mainBoard[spotx][spoty] = 1
                       text = "(%s, %s), \n" %(spotx, spoty)
                       f.write(text)

            elif event.type == KEYDOWN:
                if event.key == K_m:
                    editing = False
                
                else:
                    pass
                
            elif event.type == QUIT:
                terminate()

            pygame.display.update()
            FPSCLOCK.tick(FPS)

    f.close()
    terminate()
  
def getSpotClicked(x, y):
    for tileX in range(BOARDWIDTH):
        for tileY in range(BOARDHEIGHT):
            left, top = editedMap.getLeftTopOfBlock(tileX, tileY)
            tileRect = pygame.Rect(left, top, TILESIZE, TILESIZE)
            if tileRect.collidepoint(x, y):
                return (tileX, tileY)
    return (None, None)
        
def terminate():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
