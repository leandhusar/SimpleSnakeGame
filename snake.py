from shapes import *
from gameMap import *
from food import *
from player import *

#Constants
floor_color = (8, 8, 8)        #surface color
food_color = (200, 35, 30)     #prey color
brick_color = (50, 50, 50)     #Edge color

#Clock timer
delay_clock = pygame.time.Clock()
sleep = 30

#Player points
points = 0
#This var enables the insert from tail of a new square
grew_enabled = False
#Tail of the snake
tail = [0, 0]

#The game map has a square of 800 units (pixels)
WIDTH = 800
HEIGHT = 800

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Snake Game")

show_start = True
show_game_over = False
start_image = pygame.image.load("images/instructions.png")
game_over_image = pygame.image.load("images/game_over.png")

while still_alive:
    #While show_start is True, the instructions will be shown to the player
    #It will be happening until player press ENTER key
    while show_start:
        window.blit(start_image, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #In the button events, it changes the global direction. Previously the game
            #stored the current position, that one is used to compare the direction, in
            #order to prevent the possibility of the snake going in the opposite direction
            #immediately (read player.py)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    show_start = False
        pygame.display.update()

    #While show_game_over is True, the game over image will be shown
    #Close the game .-.
    while show_game_over:
        window.fill((0, 0, 0))
        window.blit(game_over_image, (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    '''
    First it checks if the body will be grwing for this for grow from
    the tail. If its value is FALSE (as game is starting) it directly will be
    catch the current direction of the player.

    It fills the screen. Then, it draws the walls, the snake and the food.
    
    (Read the next section)
    '''
    if grew_enabled:
        addSquareBody(serpent, tail)
        grew_enabled = False

    current_dir = direction
    window.fill(floor_color)
    
    #Drawing the walls using the map matrix from gameMap.py
    for y in range(40):
        for x in range(40):
            if gmap[x][y] == 1:
                squareDraw(window, brick_color, (x*20, y*20), 20)
    
    #Drawing the snake player (read snake.py)
    snakeDraw(window, snake_color, serpent)
    
    #Drawing the food. Using the food position only
    circleDraw(window, food_color, (food_position[0]*20 + 10, food_position[1]*20 + 10), 9)

    '''
    For now, it executes the snake movement in funtion of the current direction.
    Next, it takes the SNAKE_STATE, that refers to what thing is under the snake head.
    It would be read like this:

    0: Turns on the SHOW_GAME_OVER var. It means the player loses by colliding
       with a wall
    1: Add a point when player is over the food, activates the growing of the snake,
       stores the snake tail at TAIL position list, and change the food position
    2: Just like 0
    '''
    #View of the snake movements (read this function at player.py)
    moveSnake(serpent, direction)

    snake_state = checkHead(serpent, gmap, direction, food_position)
    if snake_state == 0:
        show_game_over = True
    elif snake_state == 1:
        points += 1
        grew_enabled = True
        tail[0] = serpent[0][0]
        tail[1] = serpent[0][1]
        food_position = changeFoodPosition(serpent)
    elif snake_state == 2:
        show_game_over = True

    #Events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #In the button events, it changes the global direction. Previously the game
        #stored the current position, that one is used to compare the direction, in
        #order to prevent the possibility of the snake going in the opposite direction
        #immediately (read player.py)
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