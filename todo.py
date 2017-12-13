import pygame

pygame.init()

size = width, height = 800, 1080

color = 40,190,130

screen = pygame.display.set_mode(size)

ball = pygame.image.load("giphy.gif")
ballAction=ball.get_rect()


while True:
    key = pygame.key.get_pressed()
    print(key)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if key[pygame.K_LEFT]:
        ballAction = ballAction.move()



    screen.fill(color)
    screen.blit(ball, ballAction)
    pygame.display.flip()
    pygame.display.set_caption("Crazy frog")







