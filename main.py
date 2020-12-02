from snake import *
from maps import *
from pigeon import *

WIDTH = 800
HEIGHT = 800

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
    clock, sleep = pygame.time.Clock(), 12
    game_over = False

    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Simple Snake Game')
    showInstructions(window)

    snake = Snake()
    game_map = GameMap()
    game_map.game_map = map_level1
    pigeon = Pigeon()

    while snake.is_alive:
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
            sleep += 1
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

def main():
    level1()

if __name__ == "__main__":
    main()