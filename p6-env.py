import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
ball_x = 300
ball_y = 100
ball_speed = 4
paddle_x = 240
paddle_y = 560
paddle_width = 120
run = True
while run:
    clock.tick(60)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 7
    if keys[pygame.K_RIGHT] and paddle_x < 480:
        paddle_x += 7
    ball_y += ball_speed
    if paddle_y < ball_y + 20 < paddle_y + 15 and paddle_x < ball_x < paddle_x + paddle_width:
        ball_speed *= -1
    pygame.draw.rect(screen, (0, 255, 0), (paddle_x, paddle_y, paddle_width, 15))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), 20)
    pygame.display.flip()
pygame.quit()
