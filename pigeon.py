from shapes import *
import random

class Pigeon:
    #Every pigeon initializes at 10 - 10 position
    def __init__(self):
        self.position = [10, 10]
    
    #It draws the pigeon by multiplying its position with 20
    def drawOnMap(self, window):
        drawPigeon(window, (self.position[0]*20, self.position[1]*20))
    
    #while exists any coincidence between pigeon, walls and snake, it will change the pigeons position
    def changePosition(self, snake, game_map):
        posX = random.randint(1, 38)
        posY = random.randint(1, 38)
        temporal_pos = [posX, posY]
        while(self.checkSnakeCoincidence(temporal_pos, snake, game_map)):
            posX = random.randint(1, 38)
            posY = random.randint(1, 38)
            temporal_pos = [posX, posY]
        self.position = [posX, posY]
        
    def checkSnakeCoincidence(self, temporal_pos, snake, game_map):
        for square in snake:
            if square == temporal_pos:
                return True
        if game_map[temporal_pos[1]][temporal_pos[0]] == 1:
            return True
        return False