import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('lolol')
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)


playerImg = pygame.image.load("spaceship.png")
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 370
playerY = 480


def player(x, y):
    screen.blit(playerImg, (x, y))

PlayerX_change = 0

running = True
while running:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                PlayerX_change = -0.1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                PlayerX_change = 0.1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                PlayerX_change = 0

    playerX = playerX + PlayerX_change

    player(playerX, playerY)







    pygame.display.update()