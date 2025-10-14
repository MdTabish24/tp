import pygame
import random
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Bouncing Ball Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 22)
ball_x = 300
ball_y = 300
ball_speed_x = 4 * random.choice([-1, 1])
ball_speed_y = -4
paddle_x = 240
paddle_y = 560
paddle_width = 120
score = 0
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
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    if ball_x <= 20 or ball_x >= 580:
        ball_speed_x *= -1
    if ball_y <= 20:
        ball_speed_y *= -1
    if paddle_y < ball_y + 20 < paddle_y + 15 and paddle_x < ball_x < paddle_x + paddle_width:
        ball_speed_y *= -1
        score += 1
    if ball_y > 600:
        run = False
    pygame.draw.rect(screen, (0, 255, 0), (paddle_x, paddle_y, paddle_width, 15))
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), 20)
    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
    pygame.display.flip()
pygame.quit()
