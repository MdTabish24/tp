import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
block = 10
x, y = 400, 300
dx, dy = 0, 0
snake = []
length = 1
food_x = random.randrange(0, 790, block)
food_y = random.randrange(0, 590, block)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx, dy = -block, 0
            elif event.key == pygame.K_RIGHT:
                dx, dy = block, 0
            elif event.key == pygame.K_UP:
                dy, dx = -block, 0
            elif event.key == pygame.K_DOWN:
                dy, dx = block, 0
    x += dx
    y += dy
    if x >= 800 or x < 0 or y >= 600 or y < 0:
        run = False
    head = [x, y]
    snake.append(head)
    if len(snake) > length:
        del snake[0]
    for part in snake[:-1]:
        if part == head:
            run = False
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (213, 50, 80), [food_x, food_y, block, block])
    for part in snake:
        pygame.draw.rect(screen, (0, 255, 0), [part[0], part[1], block, block])
    pygame.display.update()
    if x == food_x and y == food_y:
        food_x = random.randrange(0, 790, block)
        food_y = random.randrange(0, 590, block)
        length += 1
    clock.tick(15)
pygame.quit()
