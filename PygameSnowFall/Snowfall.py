import sys
import pygame
import random
import time

MAX_X: int = 1920
MAX_Y: int = 1080
MAX_SNOW: int = 200
SNOW_SIZE: int = 64


class Snow():
    def __init__(self, x, y):
        self.x = x
        self.y = y
       # self.speed = random.randint(1, 3)
        self.speed_y = random.randint(1, 3)
        self.speed_x = random.randint(-1, 1) / 2
        self.img_num = random.randint(1, 4)
        self.image_filename = f'snow{self.img_num}.png'
        self.image = pygame.image.load(self.image_filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (SNOW_SIZE, SNOW_SIZE))

    def move_snow(self):
    #    i = random.randint(1, 2)
        self.y += self.speed_y
        if self.y > MAX_Y:
            self.y = -SNOW_SIZE
        self.x += self.speed_x
        if self.x > MAX_X:                              ##  if i == 1: # MOVE right
            self.x = -SNOW_SIZE                     ##     self.x+=1
        elif self.x < -SNOW_SIZE:                                 ##    if self.x > MAX_X:
            self.x = MAX_X                                ###       self.x = -SNOW_SIZE
                                                           ## elif i == 2: #move left
                                                            ##     self.x-=1
    def draw_snow(self):                                    ##     if self.x < -SNOW_SIZE:
        screen.blit(self.image,(self.x,self.y))             ##          self.x = MAX_X+SNOW_SIZE

def initialize_snow(MAX_SNOW,snowfall):
    for i in range(0, MAX_SNOW):
        xx = random.randint(0, MAX_X)
        yy = random.randint(0, MAX_Y)
        snowfall.append(Snow(xx,yy))

def check_for_exit():
    for events in pygame.event.get():
        if events.type == pygame.KEYDOWN:
            sys.exit()

# ==================MAIN==============

pygame.init()
screen = pygame.display.set_mode((MAX_X,MAX_Y),pygame.FULLSCREEN)
bg_color = (0,0,0)
snowfall = []
initialize_snow(MAX_SNOW, snowfall)

while True:
    screen.fill(bg_color)
    check_for_exit()
    for i in snowfall:
        i.move_snow()
        i.draw_snow()
    time.sleep(0.002)
    pygame.display.flip()
