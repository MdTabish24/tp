import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Camera Shake Example")
clock = pygame.time.Clock()
world = pygame.Surface((800, 600))
shake_duration = 0
shake_power = 10
offset_x = 0
offset_y = 0
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            shake_duration = 20
    if shake_duration > 0:
        offset_x = random.randint(-shake_power, shake_power)
        offset_y = random.randint(-shake_power, shake_power)
        shake_duration -= 1
    else:
        offset_x = 0
        offset_y = 0
    world.fill((255, 255, 255))
    pygame.draw.rect(world, (255, 0, 0), (375, 275, 50, 50))
    screen.fill((0, 0, 0))
    screen.blit(world, (offset_x, offset_y))
    pygame.display.flip()
pygame.quit()
