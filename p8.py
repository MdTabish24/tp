import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Shooting Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsans", 30)
player = pygame.Rect(375, 550, 50, 40)
bullets = []
enemies = []
score = 0
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < 750:
        player.x += 5
    if keys[pygame.K_SPACE] and len(bullets) < 5:
        bullets.append(pygame.Rect(player.x + 23, player.y, 5, 10))
    for bullet in bullets[:]:
        bullet.y -= 7
        if bullet.y < 0:
            bullets.remove(bullet)
        else:
            for enemy in enemies[:]:
                if bullet.colliderect(enemy):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 1
                    break
    while len(enemies) < 5:
        enemies.append(pygame.Rect(random.randint(0, 750), 0, 50, 40))
    for enemy in enemies[:]:
        enemy.y += 2
        if enemy.y > 600:
            enemies.remove(enemy)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player)
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 0, 0), bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, (0, 255, 0), enemy)
    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
    pygame.display.update()
pygame.quit()
