from snake import *
from maps import *
from pigeon import *

WIDTH = 800
HEIGHT = 800

#This funtion needs a window to get the screen to show the image of instructions
def showInstructions(window):
    show_start = True
    while show_start:
        window.blit(pygame.image.load('images\instructions.png'), (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    show_start = False
        pygame.display.update()

def level1():
    #First, it takes the timer and set GAME_OVER var to false, score equals 0,
    #creates the snake, import map game and the audio clip to be use when the pigeon is reached
    #Shows the instructions before the game starts
    clock, sleep = pygame.time.Clock(), 12
    game_over = False

    score = 0

    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Simple Snake Game')
    showInstructions(window)

    snake = Snake()
    game_map = GameMap()
    game_map.game_map = map_level1
    pigeon = Pigeon()
    pygame.mixer.music.load('audio/chicken.mp3')

    #Change the the value X from score < X in order to take a short performance sample :)
    #Checks if the snake is able to grow its body. Then, draws the map, walls and snake body
    #moves the snake and checks whats under its head:
    #If its over a wall or on itself, the game will finish
    #If its over a pigeon, it plays the preloaded sound (chicken XD), switchs the grow ability to true, adds a point and augments the speed in 2 units
    #and changes the pigeons position
    while snake.is_alive and score < 5:
        if snake.grew_enabled:
            snake.addBody()

        window.fill((0, 0, 10))
        game_map.drawMap(window)
        pigeon.drawOnMap(window)
        snake.drawSnake(window)

        snake.move()
        snake_state = snake.checkHead(game_map.game_map, pigeon.position)
        if snake_state == ON_WALL or snake_state == ON_ITSELF:
            snake.is_alive = False
            game_over = True
        elif snake_state == ON_PIGEON:
            snake.grew_enabled = True
            score += 1
            pygame.mixer.music.play()
            sleep += 2
            pigeon.changePosition(snake.body, game_map.game_map)

        #Events:
        #Snake will move to the direction of the pressed key (its intuitive to read)
        #When spacebar key is pressed, snake sticks out its tongue.
        #Unlike the head, with the tongue it is verified that the tongue is on the wall or on the pigeon
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.changeDirection(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.changeDirection(RIGHT)
                elif event.key == pygame.K_DOWN:
                    snake.changeDirection(DOWN)
                elif event.key == pygame.K_UP:
                    snake.changeDirection(UP)
                elif event.key == pygame.K_SPACE:
                    tongue_position = snake.showTongue(window)
                    tongue_state = snake.checkTongue(tongue_position, game_map.game_map, pigeon.position)
                    if tongue_state == ON_WALL:
                        snake.is_alive = False
                        game_over = True
                    elif tongue_state == ON_PIGEON:
                        snake.grew_enabled = True
                        score += 1
                        pygame.mixer.music.play()
                        sleep += 2
                        pigeon.changePosition(snake.body, game_map.game_map)
        clock.tick(sleep)
        pygame.display.update()

    return (score, snake.is_alive)

#Level 2 seems like level one. It only changes the map
def level2():
    clock, sleep = pygame.time.Clock(), 12
    game_over = False

    score = 0

    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Simple Snake Game')

    snake = Snake()
    game_map = GameMap()
    game_map.game_map = map_level2
    pigeon = Pigeon()
    pygame.mixer.music.load('audio/chicken.mp3')

    while snake.is_alive and score < 5:
        if snake.grew_enabled:
            snake.addBody()

        window.fill((50, 30, 10))
        game_map.drawMap(window)
        pigeon.drawOnMap(window)
        snake.drawSnake(window)

        snake.move()
        snake_state = snake.checkHead(game_map.game_map, pigeon.position)
        if snake_state == ON_WALL or snake_state == ON_ITSELF:
            snake.is_alive = False
            game_over = True
        elif snake_state == ON_PIGEON:
            snake.grew_enabled = True
            score += 1
            pygame.mixer.music.play()
            sleep += 2
            pigeon.changePosition(snake.body, game_map.game_map)

        #Event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.changeDirection(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.changeDirection(RIGHT)
                elif event.key == pygame.K_DOWN:
                    snake.changeDirection(DOWN)
                elif event.key == pygame.K_UP:
                    snake.changeDirection(UP)

        clock.tick(sleep)
        pygame.display.update()
    
    return (score, snake.is_alive)

#Show game over returns a boolean value. It depends on the R key is pressed
def showGameOver():
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Simple Snake Game')

    show_start = True
    while show_start:
        window.blit(pygame.image.load('images\game_over.png'), (0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
        pygame.display.update()

#First, evalue if player wants to restart the game (on both levels)
#level_1 takes the returned value of level1. If snake is still alive, goes to level2 and repeats the same procedure
#In another case, it executes the showGameOver in order to ask to the player if it wants to play aganin
def main():
    restart = True
    while restart:
        level_1 = level1()
        if level_1[1] == True:
            level_2 = level2()
            if level_2[1] == False:
                restart = showGameOver()
        else: restart = showGameOver()

if __name__ == "__main__":
    main()