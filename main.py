import pygame

pygame.init()
screenX = 800
screenY = 600
screen = pygame.display.set_mode((screenX, screenY), pygame.FULLSCREEN)
#, pygame.FULLSCREEN
pygame.display.set_caption('lolol')
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)


playerImg = pygame.image.load("spaceship.png")
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = screenX/2
playerY = 480

EnemyImg = pygame.image.load("alien.png")
EnemyImg = pygame.transform.scale(EnemyImg, (64, 64))
EnemyX = 370
EnemyY = 50

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(EnemyImg, (x, y))
mouse_pos1 = 0
PlayerX_change = 0
running = True
new_mouse_pos = 0
while running:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        

        
        if pygame.mouse.get_pressed():
            #pygame.mouse.set_visible(False)
            mouse_pos = list(pygame.mouse.get_pos())[0] - screenX/2
            
            if mouse_pos >=screenX/2-10:
                try:
                    mouse_pos1 = new_mouse_pos
                except NameError:
                    mouse_pos1 = mouse_pos
                pygame.mouse.set_pos(screenX/2, screenY/2)

            if mouse_pos <=-screenX/2+10:
                try:
                    mouse_pos1 = new_mouse_pos
                except NameError:
                    mouse_pos1 = mouse_pos
                pygame.mouse.set_pos(screenX/2, screenY/2)

            #try:
            new_mouse_pos = mouse_pos1 + mouse_pos
            #except NameError:
            #    new_mouse_pos = mouse_pos
            
            #if mouse_pos <=50:
            #    mouse_pos1 = mouse_pos
            #    pygame.mouse.set_pos(screenX/2, screenY/2)
            
            
            #print(new_mouse_pos)
            PlayerX_change = new_mouse_pos * 0.001
            


        #if event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        #        PlayerX_change = -0.1
        #    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        #        PlayerX_change = 0.1
#
        #if event.type == pygame.KEYUP:
        #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
        #        PlayerX_change = 0

    playerX = playerX + PlayerX_change

    print(playerX)
    if playerX < -32:
        playerX = screenX-32
    if playerX > screenX-32:
        playerX = -32

    enemy(EnemyX, EnemyY)
    player(playerX, playerY)






    pygame.display.update()