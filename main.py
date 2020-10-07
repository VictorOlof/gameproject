import pygame
import random


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Snake:
    def __init__(self, x, y, x_change, y_change, block_size, color, screen):
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change
        self.block_size = block_size
        self.color = color
        self.screen = screen
        self.length = [(self.x, self.y)]

    def move(self):
        self.x += self.x_change
        self.y += self.y_change
        self.length.append((self.x, self.y))
        self.length.pop(0)

    def draw(self):
        # pygame.draw.rect(self.screen, self.color, [self.x, self.y, self.block_size, self.block_size])
        for item in self.length:
            pygame.draw.rect(self.screen, self.color, [item[0], item[1], self.block_size, self.block_size])


class Food:
    def __init__(self, x, y, block_size, color, screen):
        self.x = x
        self.y = y
        self.block_size = block_size
        self.color = color
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, WHITE, [self.x, self.y, self.block_size, self.block_size])

    def new_position(self, snake_block):
        self.x = random.randrange(0, SCREEN_WIDTH, snake_block)
        self.y = random.randrange(0, SCREEN_WIDTH, snake_block)


def main():
    pygame.init()

    # open a window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake game")
    screen.fill(BLACK)

    # run the game
    game_over = False
    clock = pygame.time.Clock()

    # create snake object
    snake_block = 10
    snake = Snake(200, 200, 0, 0, snake_block, WHITE, screen)
    food = Food(100, 100, snake_block, WHITE, screen)

    while not game_over:
        # inputs from user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    snake.y_change = snake_block
                    snake.x_change = 0
                if event.key == pygame.K_UP:
                    snake.y_change = -snake_block
                    snake.x_change = 0
                if event.key == pygame.K_LEFT:
                    snake.x_change = -snake_block
                    snake.y_change = 0
                if event.key == pygame.K_RIGHT:
                    snake.x_change = snake_block
                    snake.y_change = 0

        screen.fill(BLACK)
        snake.move()
        if not 0 <= snake.x < SCREEN_WIDTH:
            game_over = True
        if not 0 <= snake.y < SCREEN_HEIGHT:
            game_over = True

        if snake.x == food.x and snake.y == food.y:
            snake.length.append((snake.x, snake.y))
            food.new_position(snake_block)

        snake.draw()
        food.draw()

        pygame.display.update()
        clock.tick(10)
    pygame.display.update()


if __name__ == '__main__':
    main()
