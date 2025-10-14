#P2 A --------------------------------------------
import pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((255, 0, 0))
    pygame.display.flip()
    clock.tick(3)
pygame.quit()
#P2 B --------------------------------------------
import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill('lightblue')
    pygame.draw.circle(screen, "red", (640, 360), 100)
    pygame.display.update()
pygame.quit()
#P2 C --------------------------------------------
import pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
x, y = 300, 200
dx, dy = 0, 0
block = 20
snake = []
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
                dx, dy = 0, -block
            elif event.key == pygame.K_DOWN:
                dx, dy = 0, block
    x += dx
    y += dy
    snake.append([x, y])
    if len(snake) > 1:
        del snake[0]
    screen.fill((255, 255, 255))
    for part in snake:
        pygame.draw.rect(screen, (0, 255, 0), [part[0], part[1], block, block])
    pygame.display.flip()
    clock.tick(10)
pygame.quit()
