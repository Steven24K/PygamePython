import pygame
import random
import sys

pygame.init()
pygame.font.init()

size = width, height = 1200, 800

color = 40,190,130

speed = 5
score = 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("giphy.gif")
enemy = pygame.image.load("enemy.png")
default_font = pygame.font.SysFont(None,30)

ballAction=ball.get_rect()
enemyAction = enemy.get_rect()
enemyAction.x = random.randint(0,width)
enemyAction.y = random.randint(0, height)


while True:
    screen.fill(color)

    key = pygame.key.get_pressed()
    display_score = default_font.render("Score: " + str(score), False,(0,0,0))
    #print(key)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if key[pygame.K_LEFT]:
        ballAction = ballAction.move(-speed,0)
    if key[pygame.K_RIGHT]:
        ballAction = ballAction.move(speed,0)
    if key[pygame.K_UP]:
        ballAction = ballAction.move(0,-speed)
    if key[pygame.K_DOWN]:
        ballAction = ballAction.move(0,speed)

    if ballAction.x + ballAction.width < 0:
        ballAction.x = width
    if ballAction.x > width:
        ballAction.left = -ballAction.width
    if ballAction.y + ballAction.height < 0:
        ballAction.y = height
    if ballAction.y > height:
        ballAction.top = -ballAction.height

    print("My position: (" + str(ballAction.x) + "," + str(ballAction.y) + ")")
    print("Enemy position: (" + str(enemyAction.x) + "," + str(enemyAction.y) + ")")
    # if ballAction.x + ballAction.width <= enemyAction.x or ballAction.x >= enemyAction.x + enemyAction.width or ballAction.y + ballAction.height <= enemyAction.y or ballAction.y >= enemyAction.y + enemyAction.height:
    #     screen.blit(enemy, enemyAction)
    if ballAction.x + ballAction.width > enemyAction.x and ballAction.x < enemyAction.x + enemyAction.width and ballAction.y + ballAction.height > enemyAction.y and ballAction.y < enemyAction.y + enemyAction.height:
        enemyAction.x = random.randint(1, width- enemyAction.width)
        enemyAction.y = random.randint(1, height-enemyAction.height)
        score += 1
        
        print("Got that little devil...")

    screen.blit(ball, ballAction)
    screen.blit(display_score, (10,10))
    screen.blit(enemy, enemyAction)
    pygame.display.flip()
    pygame.display.set_caption("Crazy frog")







