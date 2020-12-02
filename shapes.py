import pygame, sys
from pygame.locals import *

'''
This function draws a filled square in a WINDOW. It receives a color (R, G, B)
tuple, another (POSX, POSY) tuple that indicates the position of the upper left corner,
and finally its sides lenght
'''
def drawSquare(window, color, position, length):
    pygame.draw.rect(window, color, (position[0]*length, position[1]*length, length, length))

def drawBrick(window, position):
    window.blit(pygame.image.load('images/brick.png'), position)

def drawPigeon(window, position):
    window.blit(pygame.image.load('images/pigeon.png'), position)