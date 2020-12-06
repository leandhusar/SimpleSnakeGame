from shapes import *

#Directions as constants
UP = 'up'
DOWN = 'down'
RIGHT = 'right'
LEFT = 'left'

ON_WALL = 0
ON_PIGEON = 1
ON_ITSELF = 2

class Snake:
    def __init__(self):
        self.is_alive = True
        self.color = (255, 153, 0)
        self.direction = RIGHT
        self.body = [[1, 1], [2, 1], [3, 1]]
        self.grew_enabled = False
        self.tail = [self.body[0][0], self.body[0][1]]

    '''
    This method draws the snake on a WINDOW, using a color (R, G, B) tuple,
    and the list that contains every position of each square of its body.
    The square lenght is 20 pixels
    '''
    def drawSnake(self, window):
        for square in self.body:
            drawSquare(window, self.color, square, 20)
    
    def checkHead(self, game_map, food_position):
        head = self.body[-1]
        if game_map[head[1]][head[0]] == 1:
            return 0
        elif head == food_position:
            return 1
        elif self.checkAutoCollide():
            return 2
    '''
    It checks if the head is not colliding with any part of the snake
    ignoring its head
    '''
    def checkAutoCollide(self):
        for i in range(len(self.body)-1):
            if self.body[-1] == self.body[i]:
                return True
        return False

    def move(self):
        self.moveUntilHead()
        if self.direction == UP:
            self.body[-1][1] = self.body[-1][1] - 1
        elif self.direction == DOWN:
            self.body[-1][1] = self.body[-1][1] + 1
        elif self.direction == RIGHT:
            self.body[-1][0] = self.body[-1][0] + 1
        elif self.direction == LEFT:
            self.body[-1][0] = self.body[-1][0] - 1
        self.tail = [self.body[0][0], self.body[0][1]]
    
    def moveUntilHead(self):
        for i in range(len(self.body)-1):
            self.body[i] = self.body[i+1][:]
        
    def changeDirection(self, new_direction):
        if self.direction == UP and new_direction != DOWN:
            self.direction = new_direction
        elif self.direction == DOWN and new_direction != UP:
            self.direction = new_direction
        elif self.direction == RIGHT and new_direction != LEFT:
            self.direction = new_direction
        elif self.direction == LEFT and new_direction != RIGHT:
            self.direction = new_direction
    
    def addBody(self):
        self.body.insert(0, self.tail[:])
        self.grew_enabled = False
    
    def showTongue(self, window):
        tongue = 'images/tongue_' + self.direction + '.png'
        if self.direction == UP:
            position = [self.body[-1][0], self.body[-1][1]-1]
        elif self.direction == DOWN:
            position = [self.body[-1][0], self.body[-1][1]+1]
        elif self.direction == RIGHT:
            position = [self.body[-1][0]+1, self.body[-1][1]]
        elif self.direction == LEFT:
            position = [self.body[-1][0]-1, self.body[-1][1]]
        drawTongue(window, (position[0]*20, position[1]*20), tongue)
        return [position[0], position[1]]

    def checkTongue(self, position, game_map, food_position):
        if game_map[position[1]][position[0]] == 1:
            return 0
        elif position == food_position:
            return 1   