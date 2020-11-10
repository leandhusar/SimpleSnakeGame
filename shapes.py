import pygame, sys
from pygame.locals import *

'''
This function draws a filled circle in a WINDOW. It receives a color (R, G, B)
tuple, another (POSX, POSY) tuple that indicates the circle center. Finally
it takes the circle radius
'''
def circleDraw(window, color, position, radius):
    pygame.draw.circle(window, color, position, radius)

'''
This function draws a filled square in a WINDOW. It receives a color (R, G, B)
tuple, another (POSX, POSY) tuple that indicates the position of the upper left corner,
and finally its sides lenght
'''
def squareDraw(window, color, position, length):
    pygame.draw.rect(window, color, (position[0], position[1], length, length))