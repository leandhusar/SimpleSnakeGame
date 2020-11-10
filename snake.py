from shapes import *
from gameMap import *
from food import *
from player import *

#Constants
floor_color = (8, 8, 8)   #surface color
food_color = (200, 35, 30)       #prey color
brick_color = (50, 50, 50)     #Edge color

#Clock timer
delay_clock = pygame.time.Clock()
sleep = 30

#Player points
points = 0

#The game map has a square of 800 units (pixels)
WIDTH = 800
HEIGHT = 800

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Snake Game")

while still_alive:
    current_dir = direction
    window.fill(floor_color)
    
    #Drawing the walls
    for y in range(40):
        for x in range(40):
            if gmap[x][y] == 1:
                squareDraw(window, brick_color, (x*20, y*20), 20)
    
    #Drawing the snake player
    snakeDraw(window, snake_color, serpent)
    
    #Drawing the food
    circleDraw(window, food_color, (food_position[0]*20 + 10, food_position[1]*20 + 10), 9)

    #View of the snake movements
    moveSnake(serpent, direction)

    snake_state = checkHead(serpent, gmap, direction, food_position)
    if snake_state == 0:
        still_alive = False
    elif snake_state == 1:
        points += 1
        food_position = changeFoodPosition(serpent)
    elif snake_state == 2:
        still_alive = False

    #Events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = LEFT
            elif event.key == pygame.K_RIGHT:
                direction = RIGHT
            elif event.key == pygame.K_DOWN:
                direction = DOWN
            elif event.key == pygame.K_UP:
                direction = UP

    direction = changeDirection(current_dir, direction)
    #Using the clock space time
    delay_clock.tick(sleep)
    #Updating the screen
    pygame.display.update()