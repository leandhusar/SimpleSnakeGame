from shapes import *
from food import *

#Constants: Snake directions
UP = "up"
DOWN = "down"
RIGHT = "right"
LEFT = "left"

still_alive = True
snake_color = (60, 170, 30)     #Snake color
serpent = [[1, 1], [2, 1], [3, 1]]
direction = RIGHT

'''
This function draws the snake on a WINDOW, using a color (R, G, B) tuple,
and the list that contains every position of each square of its body.
The square lenght is 20 pixels
'''
def snakeDraw(window, color, body):
    for square in body:
        squareDraw(window, snake_color, (square[0]*20, square[1]*20), 20)

'''
This function catchs the snake head by taking its last position
of the BODY list
'''
def checkHead(body, gmap, snake_dir, food_pos):
    head = body[len(body)-1]
    if gmap[head[1]][head[0]] == 1:
        return 0                             #0 means player loses the game by colliding with a wall
    elif head == food_pos:
        return 1                             #1 means player wins 1 point
    elif checkAutocollide(body) == True:
        return 2                             #2 means player loses the game by colliding with itself

def moveSnake(body, direction):
    moveUntilHead(body)
    if direction == UP:
        body[len(body)-1][1] = body[len(body)-1][1] - 1
    elif direction == DOWN:
        body[len(body)-1][1] = body[len(body)-1][1] + 1
    elif direction == RIGHT:
        body[len(body)-1][0] = body[len(body)-1][0] + 1
    elif direction == LEFT:
        body[len(body)-1][0] = body[len(body)-1][0] - 1

def moveUntilHead(body):
    for i in range(len(body)-1):
        body[i] = body[i+1][:]

def checkAutocollide(body):
    for i in range(len(body)-1):
        if body[-1] == body[i]:
            return True
    return False

def changeDirection(actual, new_direction):
    if actual == UP:
        if new_direction == DOWN:
            return actual
    elif actual == DOWN:
        if new_direction == UP:
            return actual
    elif actual == RIGHT:
        if new_direction == LEFT:
            return actual
    elif actual == LEFT:
        if new_direction == RIGHT:
            return actual
    return new_direction

def addSquareBody(body, square_pos):
    body.insert(0, square_pos[:])