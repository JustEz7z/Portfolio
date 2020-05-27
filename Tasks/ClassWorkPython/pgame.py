import pygame
pygame.init()
gameDisplay=pygame.display.set_mode((400,300))
pygame.display.set_caption("My first game")
clock=pygame.time.Clock()
crashed=False

jumpCount = 10

x=25
y=25
width=40
height=60
vol=5

while not crashed:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 25:
        x=x-vol
    elif keys[pygame.K_RIGHT] and x < 375:
        x = x+vol
    elif keys[pygame.K_UP] and y > 25:
        y = y-vol
    elif keys[pygame.K_DOWN] and y < 275:
        y = y+vol
    elif keys[pygame.K_SPACE]:
        y -= (jumpCount ** 2) / 5
    gameDisplay.fill((0,0,0))
    pygame.draw.circle(gameDisplay,(255,255,255),(x,y),25)

    pygame.display.update()

    clock.tick(60)

pygame.quit()