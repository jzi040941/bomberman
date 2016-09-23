import pygame, sys
from pygame.locals import *

sys.path.append("C:/Python32/bomberman/game")

import settings, game_system, runGame
from settings import *
from game_system import *
from runGame import *

def startScreen(surf, font, fps):
    FPSCLOCK = fps
    TITLE_IMG = pygame.image.load('C:/Python32/bomberman/sprite/title.png')
    
    titleRect = TITLE_IMG.get_rect()
    topCoord = 300
    titleRect.top = topCoord
    titleRect.centerx=HALF_WINWIDTH
    topCoord += titleRect.height
    
    instructionText=['Press any key to start.']
    surf.fill(BLACK)
    surf.blit(TITLE_IMG, titleRect)
    
    # Position and draw the text.
    for i in range(len(instructionText)):
        instSurf = font.render(instructionText[i], 1, TEXTCOLOR)
        instRect = instSurf.get_rect()
        topCoord += 10 # 10 pixels will go in between each line of text.
        instRect.top = topCoord
        instRect.centerx = HALF_WINWIDTH
        topCoord += instRect.height # Adjust for the height of the line.
        surf.blit(instSurf, instRect)

    while True: # Main loop for the start screen.
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYUP:
                if event.key == K_ESCAPE:
                    terminate()
                return # user has pressed a key, so return.

        # Display the DISPLAYSURF contents to the actual screen.
        pygame.display.update()
        FPSCLOCK.tick()
        
def chooseCharacter(surf, fps):
    FPSCLOCK = fps
    CHARACTER_IMG = pygame.image.load('C:/Python32/bomberman/sprite/character.png')
    ARROW1_IMG = pygame.image.load('C:/Python32/bomberman/sprite/arrow1.png')
    ARROW2_IMG = pygame.image.load('C:/Python32/bomberman/sprite/arrow2.png')
    ARROWR_IMG = pygame.image.load('C:/Python32/bomberman/sprite/arrowR.png')
    characterRect = CHARACTER_IMG.get_rect()
    topCoord = 40
    characterRect.top = topCoord
    characterRect.centerx = HALF_WINWIDTH
    topCoord+=characterRect.height
    
    CHA1_SURF = pygame.font.Font('freesansbold.ttf', 32).render('CHARACTER 1', True, TEXTCOLOR, BLACK)
    CHA1_RECT = CHA1_SURF.get_rect()
    CHA1_RECT.center = (int(WINDOWWIDTH / 2-300), int(WINDOWHEIGHT / 2) + 200)
    
    CHA2_SURF = pygame.font.Font('freesansbold.ttf', 32).render('CHARACTER 2', True, TEXTCOLOR, BLACK)
    CHA2_RECT = CHA2_SURF.get_rect()
    CHA2_RECT.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 200)
    
    CHA3_SURF = pygame.font.Font('freesansbold.ttf', 32).render('CHARACTER 3', True, TEXTCOLOR, BLACK)
    CHA3_RECT = CHA3_SURF.get_rect()
    CHA3_RECT.center = (int(WINDOWWIDTH / 2+300), int(WINDOWHEIGHT / 2) + 200)

    arrow1centers=[(CHA1_RECT.center[0], CHA1_RECT.center[1]+50), (CHA2_RECT.center[0], CHA2_RECT.center[1]+50), (CHA3_RECT.center[0], CHA3_RECT.center[1]+50)]
    arrow2centers=[(CHA1_RECT.center[0], CHA1_RECT.center[1]+100), (CHA2_RECT.center[0], CHA2_RECT.center[1]+100), (CHA3_RECT.center[0], CHA3_RECT.center[1]+100)]
    arrow1Rect=ARROW1_IMG.get_rect()
    arrow2Rect=ARROW2_IMG.get_rect()
    arrow1x=0
    arrow2x=0
    arrowR1=0
    arrowR2=0
    
    while True:
        for event in pygame.event.get(QUIT):
            terminate()
        for event in pygame.event.get(KEYUP):
            if event.key == K_ESCAPE:
                terminate()
            if arrowR1==0:
                if event.key == K_d:
                    if arrow1x!=2:
                        arrow1x=arrow1x+1
                if event.key==K_a:
                    if arrow1x!=0:
                        arrow1x=arrow1x-1
                if event.key==K_g:
                    arrowR1=1
            if arrowR2==0:
                if event.key == K_RIGHT:
                    if arrow2x!=2:
                        arrow2x=arrow2x+1
                if event.key==K_LEFT:
                    if arrow2x!=0:
                        arrow2x=arrow2x-1
                if event.key==K_RETURN:
                    arrowR2=1
            #pygame.event.post(event)
                
        surf.fill(SCREENCOLOR)
        surf.blit(CHARACTER_IMG, characterRect)
        surf.blit(CHA1_SURF, CHA1_RECT)
        surf.blit(CHA2_SURF, CHA2_RECT)
        surf.blit(CHA3_SURF, CHA3_RECT)
        arrow1Rect.center=arrow1centers[arrow1x]
        arrow2Rect.center=arrow2centers[arrow2x]
        surf.blit(ARROW1_IMG, arrow1Rect)
        surf.blit(ARROW2_IMG, arrow2Rect)
        if arrowR1==1:
            surf.blit(ARROWR_IMG, arrow1Rect)
        if arrowR2==1:
            surf.blit(ARROWR_IMG, arrow2Rect)
        
        pygame.display.update()
        FPSCLOCK.tick()
        if arrowR1==1 and arrowR2==1:
            pygame.time.delay(500)
            return (arrow1x, arrow2x)

def chooseMap(surf, fps):
    FPSCLOCK = fps
    MAP_IMG = pygame.image.load('C:/Python32/bomberman/sprite/MAP.png')
    ARROW1_IMG = pygame.image.load('C:/Python32/bomberman/sprite/arrow1.png')
    ARROWR_IMG = pygame.image.load('C:/Python32/bomberman/sprite/arrowR.png')
    mapRect = MAP_IMG.get_rect()
    topCoord = 40
    mapRect.top = topCoord
    mapRect.centerx = HALF_WINWIDTH
    topCoord+=mapRect.height
    
    MAP1_SURF = pygame.font.Font('freesansbold.ttf', 32).render('MAP 1', True, TEXTCOLOR, BLACK)
    MAP1_RECT = MAP1_SURF.get_rect()
    MAP1_RECT.center = (int(WINDOWWIDTH / 2-300), int(WINDOWHEIGHT / 2) + 200)
    
    MAP2_SURF = pygame.font.Font('freesansbold.ttf', 32).render('MAP 2', True, TEXTCOLOR, BLACK)
    MAP2_RECT = MAP2_SURF.get_rect()
    MAP2_RECT.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 200)
    
    MAP3_SURF = pygame.font.Font('freesansbold.ttf', 32).render('MAP 3', True, TEXTCOLOR, BLACK)
    MAP3_RECT = MAP3_SURF.get_rect()
    MAP3_RECT.center = (int(WINDOWWIDTH / 2+300), int(WINDOWHEIGHT / 2) + 200)

    arrow1centers=[(MAP1_RECT.center[0], MAP1_RECT.center[1]+50), (MAP2_RECT.center[0], MAP2_RECT.center[1]+50), (MAP3_RECT.center[0], MAP3_RECT.center[1]+50)]
    arrow1Rect=ARROW1_IMG.get_rect()
    
    arrow1y=0
    
    arrowR1=0
    
    
    while True:
        for event in pygame.event.get(QUIT):
            terminate()
        for event in pygame.event.get(KEYUP):
            if event.key == K_ESCAPE:
                terminate()
            if arrowR1==0:
                if event.key == K_RIGHT:
                    if arrow1y!=2:
                        arrow1y=arrow1y+1
                if event.key==K_LEFT:
                    if arrow1y!=0:
                        arrow1y=arrow1y-1
                if event.key==K_RETURN:
                    arrowR1=1
            
            #pygame.event.post(event)
                
        surf.fill(SCREENCOLOR)
        surf.blit(MAP_IMG, mapRect)
        surf.blit(MAP1_SURF, MAP1_RECT)
        surf.blit(MAP2_SURF, MAP2_RECT)
        surf.blit(MAP3_SURF, MAP3_RECT)
        arrow1Rect.center=arrow1centers[arrow1y]
        
        surf.blit(ARROW1_IMG, arrow1Rect)
        
        if arrowR1==1:
            surf.blit(ARROWR_IMG, arrow1Rect)
       
        
        pygame.display.update()
        FPSCLOCK.tick()
        if arrowR1==1 :
            pygame.time.delay(500)
            return (arrow1y)

    

def finish(surf, fps):
    # Win/Lose check/수민
    FPSCLOCK = fps
    if True:
        TEXT1 = 'Game Over'
        textSurf = pygame.font.Font('freesansbold.ttf', 60).render(TEXT1, True, BLACK)
        textRect = textSurf.get_rect()
        textRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
            
        # Display the "Play again?" text with Yes and No buttons.
        text2Surf = pygame.font.Font('freesansbold.ttf', 32).render('Play again?', True, BLACK)
        text2Rect = text2Surf.get_rect()
        text2Rect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 50)

        # Make "Yes" button.
        yesSurf = pygame.font.Font('freesansbold.ttf', 32).render('Yes', True, BLACK)
        yesRect = yesSurf.get_rect()
        yesRect.center = (int(WINDOWWIDTH / 2) - 60, int(WINDOWHEIGHT / 2) + 90)

        # Make "No" button.
        noSurf = pygame.font.Font('freesansbold.ttf', 32).render('No', True, BLACK)
        noRect = noSurf.get_rect()
        noRect.center = (int(WINDOWWIDTH / 2) + 60, int(WINDOWHEIGHT / 2) + 90)

        arrowcenters=[(yesRect.center[0]-40, yesRect.center[1]), (noRect.center[0]-40, noRect.center[1])]
        arrowSurf=pygame.font.Font('freesansbold.ttf', 32).render('>', True, BLACK)
        arrowRect=arrowSurf.get_rect()
        
        arrowselect = 0
        selecting = True


            
            

        
        while selecting:
 
            for event in pygame.event.get(): # event handling loop
                if event.type == QUIT:
                    terminate()
                    
                if event.type == KEYUP:
                    if event.key == K_RIGHT:
                        if arrowselect != 1:
                            arrowselect +=1
                    if event.key == K_LEFT:
                        if arrowselect != 0:
                            arrowselect -=1
                    if event.key == K_RETURN:
                            selecting = False
            
                            
            trans = pygame.Surface(surf.get_size())
            trans.set_alpha(5)
            trans.fill(BLOCKCOLOR)
            surf.blit(trans, (0, 0))
            surf.blit(textSurf, textRect)
            surf.blit(text2Surf, text2Rect)
            surf.blit(yesSurf, yesRect)
            surf.blit(noSurf, noRect)
        
            arrowRect.center = arrowcenters[arrowselect]
            surf.blit(arrowSurf, arrowRect)
                              
            pygame.display.update()
            FPSCLOCK.tick()
            
        if arrowselect == 1: 
            terminate()
        else:
            pass


