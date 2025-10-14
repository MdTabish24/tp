import pygame
import random
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Snow Animation")
clock = pygame.time.Clock()
snow_list = []
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x, y])
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0, 0, 0))
    for snow in snow_list:
        pygame.draw.circle(screen, (255, 255, 255), snow, 4)
        snow[1] += 1
        if snow[1] > 400:
            snow[0] = random.randrange(0, 400)
            snow[1] = random.randrange(-50, -10)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
