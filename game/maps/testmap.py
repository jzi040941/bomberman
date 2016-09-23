import pygame, sys
from pygame.locals import*

sys.path.append("C:/Python32/bomberman/game")

import map_system
from map_system import*

def testmap(board):
    normalBoard = [(7, 4),
(6, 2), 
(10, 1), 
(13, 4), 
(11, 5), 
(8, 7), 
(7, 7), 
(4, 8), 
(2, 8), 
(2, 4), 
(15, 9), 
(12, 10), 
(10, 10), 
(9, 9), 
(10, 7), 
(16, 8), 
(16, 9), 
(19, 6), 
(15, 2), 
(19, 2), 
(20, 4), 
(20, 10), 
(20, 12), 
(18, 4), 
(16, 1), 
(16, 0), 
(13, 0), 
(11, 1), 
(8, 1), 
(7, 2), 
(2, 1), 
(1, 3), 
(3, 11), 
(4, 11), 
(6, 12), 
(8, 12), 
(10, 12)]
   


    while not len(normalBoard) == 1 :
        tilePos = normalBoard.pop()
        
        tileX = tilePos[0]
        tileY = tilePos[1]

        setNormalPosition(board, tileX, tileY)

            
