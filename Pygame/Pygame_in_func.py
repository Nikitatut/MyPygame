import pygame

MAX_X = 1920
MAX_Y = 1080
game_over = False
bakground_color = (40,5,45)

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption("My First Pygame from Ntyutikov!")

myimage = pygame.image.load('spravedlivo.jpg').convert()
myimage = pygame.transform.scale(myimage,(250,200))

x=500
y=100

# ============MAIN GAME LOOP
while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            elif event.key == pygame.K_LEFT:
                x-=20
            elif event.key == pygame.K_RIGHT:
                x+=20
            elif event.key == pygame.K_UP:
                y-=20
            elif event.key == pygame.K_DOWN:
                y+=20
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

    screen.fill(bakground_color)
    screen.blit(myimage, (x,y))
    pygame.display.flip()