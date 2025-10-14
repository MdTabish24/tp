import pygame
import math
pygame.init()
screen = pygame.display.set_mode((1200, 300))
pygame.display.set_caption("Endless Scrolling in pygame")
bg = pygame.image.load("img.jpg").convert()
clock = pygame.time.Clock()
scroll = 0
tiles = math.ceil(1200 / bg.get_width()) + 1
run = True
while run:
    clock.tick(33)
    for i in range(tiles):
        screen.blit(bg, (bg.get_width() * i + scroll, 0))
    scroll -= 6
    if abs(scroll) > bg.get_width():
        scroll = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
