import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
player = pygame.Rect(375, 550, 50, 40)
bullets = []
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
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player)
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 0, 0), bullet)
    pygame.display.update()
pygame.quit()
