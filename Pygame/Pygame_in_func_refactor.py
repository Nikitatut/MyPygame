import pygame

MAX_X = 1920
MAX_Y = 1080
IMG_SIZE_X = 250
IMG_SIZE_Y = 200
x=500
y=100
game_over = False
bakground_color = (40,5,45)

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption("My First Pygame from Ntyutikov!")

myimage = pygame.image.load('spravedlivo.jpg').convert()
myimage = pygame.transform.scale(myimage,(IMG_SIZE_X,IMG_SIZE_Y))


move_right = False
move_left = False
move_up = False
move_down = False
# ============MAIN GAME LOOP
while not game_over:   #While game_over == False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True
            elif event.key == pygame.K_ESCAPE:
                game_over = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

    if move_left:   #if move_left == True
        x -= 1
        if x < 0:
            x = 0
    if move_right:
        x+=1
        if x > MAX_X-IMG_SIZE_X:
            x = MAX_X-IMG_SIZE_X
    if move_up:
        y-=1
        if y < 0:
            y = 0
    if move_down:
        y+=1
        if y > MAX_Y-IMG_SIZE_Y:
            y = MAX_Y-IMG_SIZE_Y

    screen.fill(bakground_color)
    screen.blit(myimage, (x,y))
    pygame.display.flip()