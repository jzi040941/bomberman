import pygame, sys
from pygame.locals import *

sys.path.append("C:/Python32/bomberman/game")
sys.path.append("C:/Python32/bomberman/game/maps")

import settings
from settings import *

import charcter, game_system, screen , map_system, testmap
from charcter import *
from game_system import *
from screen import *
from map_system import*
from testmap import*
from item import*

import threading

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('bomberman')
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    
    
    while True:
        startScreen(DISPLAYSURF, BASICFONT, FPSCLOCK)
        temp = chooseCharacter(DISPLAYSURF, FPSCLOCK)
        runGame()


def runGame():
    global boardLeft,boardRight,boardBottom,boardTop

    gameover=False
    #Setup
    invulnerableMode = False  # if the player is invulnerable
    invulnerableStartTime = 0 # time the player became invulnerable
    gameOverMode = False      # if the player has lost
    winMode = False           # if the player has won

    #맵 관련
    #blankTileSet
    #맵에서 빈칸인 부분의 타일X,Y 좌표를 (tileX,tiley)형식으로 가지고있는 집
    #mainBoard,blankTileSet = MAP1()
    mainBoard = generateBoard()
    testmap(mainBoard)
    
    blankTileSet = set()
    makeBlankTileSet(blankTileSet, mainBoard)

    #get Board top,left,right,bottom value
    boardLeft,boardTop = getLeftTopOfBlock(0, 0)
    boardRight,boardBottom = getLeftTopOfBlock(BOARDWIDTH-1, BOARDHEIGHT-1)
    boardRight = boardRight + TILESIZE
    boardBottom = boardBottom + TILESIZE

    #플레이어들
    players = []
    players.append(character(0,'B',2))
    players.append(character(1,'A',1))
    
    #노성훈 아이템관련
    items = []
    itemReloadTime = 10

    #timer = threading.Timer(itemReloadTime,addItem,args=(items,itemReloadTime,blankTileSet,DISPLAYSURF))
    #timer.start()
    #USEREVENT+1 <- 아이템
    pygame.time.set_timer(USEREVENT+1,itemReloadTime*1000)
    pygame.event.post(pygame.event.Event(USEREVENT+1))
    while not gameover:
        #drawBoard(DISPLAYSURF, mainBoard, '')
        displayBoard(DISPLAYSURF, mainBoard)
        

        # draw the item
        for i in range(len(items)-1, -1, -1):
            items[i].checkCollidePlayerAndEvent(players[0], players[0].rect)
            items[i].checkCollidePlayerAndEvent(players[1], players[1].rect)
            if items[i].delSignal:
                blankTileSet.add((items[i].tileX,items[i].tileY))
                del items[i]
            else:
                items[i].drawItem(DISPLAYSURF)
            

        # 플레이어, 폭탄 그리는 부분 (1p , 2p 똑같은 작업 반복)
        for player in players:
            flashIsOn = round(time.time(), 1) * 10 % 2 == 1
            if not gameOverMode and not (invulnerableMode and flashIsOn):
                player.showchar(DISPLAYSURF)
            for i in range(len(player.bombs)-1, -1, -1):
                bomb = player.bombs[i]
                bomb.show(DISPLAYSURF,players)
                if not bomb.timeCheck(time.time(),bomb.endTime) :
                    bomb.end(player)
                    gameover = bomb.collideSignal
                    #modify del bomb -> del player.bombs[i]
                    del player.bombs[i]

            
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()

            elif event.type == pygame.USEREVENT+1:
                addItem(items,itemReloadTime,blankTileSet,DISPLAYSURF)
                
            elif event.type == KEYDOWN:

                #1p 조작
                if event.key==K_w:
                    players[0].setMoveSignal(UP, True)
                elif event.key==K_s:
                    players[0].setMoveSignal(DOWN, True)
                elif event.key==K_a:
                    players[0].setMoveSignal(LEFT, True)
                elif event.key==K_d:
                    players[0].setMoveSignal(RIGHT, True)
                elif event.key==K_SPACE :
                    players[0].putbomb(DISPLAYSURF,players[0])
                    
                #2p 조작
                elif event.key ==K_UP:
                    players[1].setMoveSignal(UP, True)
                elif event.key==K_DOWN:
                    players[1].setMoveSignal(DOWN, True)
                elif event.key==K_LEFT:
                    players[1].setMoveSignal(LEFT, True)
                elif event.key==K_RIGHT:
                    players[1].setMoveSignal(RIGHT, True)
                elif event.key==K_l :
                    players[1].putbomb(DISPLAYSURF,players[1])
                    
                #게임종료 테스트
                elif event.key==K_m :
                    gameover=True
                
                    
            elif event.type == KEYUP:
                # stop moving the player's squirrel
                '''if event.key in (K_LEFT, K_a):
                    players[0].setMoveSignal(LEFT, False)
                elif event.key in (K_RIGHT, K_d):
                    players[0].setMoveSignal(RIGHT, False)
                elif event.key in (K_UP, K_w):
                    players[0].setMoveSignal(UP, False)
                elif event.key in (K_DOWN, K_s):
                    players[0].setMoveSignal(DOWN, False)'''
                if event.key ==K_UP:
                    players[1].setMoveSignal(UP, False)
                elif event.key==K_DOWN:
                    players[1].setMoveSignal(DOWN, False)
                elif event.key==K_LEFT:
                    players[1].setMoveSignal(LEFT, False)
                elif event.key==K_RIGHT:
                    players[1].setMoveSignal(RIGHT, False)
                elif event.key==K_w:
                    players[0].setMoveSignal(UP, False)
                elif event.key==K_s:
                    players[0].setMoveSignal(DOWN, False)
                elif event.key==K_a:
                    players[0].setMoveSignal(LEFT, False)
                elif event.key==K_d:
                    players[0].setMoveSignal(RIGHT, False)
                
                    
                elif event.key == K_ESCAPE:
                    terminate()

        #플레이어별 움직임 이벤트 적용
        players[0].move(mainBoard)
        players[1].move(mainBoard)

                
        #화면 업데이트
        pygame.display.update()
        FPSCLOCK.tick(FPS)
    pygame.time.set_timer(USEREVENT+1,0)
    finish(DISPLAYSURF, FPSCLOCK)
        
if __name__ == '__main__':
    main()
