import sys
import time
import pygame
from pygame.locals import *


pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

calc = 0
counter = 1

vector = [90, 23, 45, 28, 12, 54, 33, 27, 19, 11]
vt = [True]*len(vector)
position = [0]*10

size = width, height = 720, 540
black = 0, 0, 0

screen = pygame.display.set_mode(size)


class Number:
    def __init__(self, order, value, color=(255, 255, 255)):
        self.mov = True
        self.value = value
        self.color = color
        self.speed = [1, 0]
        self.order = order
        self.text = myfont.render(str(value), False, self.color)
        self.pos = self.text.get_rect().move(10, order*30+10)

    def move(self, go):
        if go == 'up position' and self.mov:
            self.pos = self.pos.move(self.speed)
            if self.pos.right == 100:
                self.speed[0] = 0
                self.speed[1] = -1
            if self.pos.top < self.order*30+10:
                self.speed[0] = 1
                self.speed[1] *= 0
            if self.pos.right > 200:
                self.speed[0] = 0
                self.mov = False

        if go == 'position' and False:
            self.pos = self.pos.move(self.speed)
            if self.pos.right > 80:
                self.speed[0] = 0

        if go == 'down position' and False:
            self.pos = self.pos.move(self.speed)
            if self.pos.right == 50:
                self.speed[0] = 0
                self.speed[1] = -1
            if self.pos.top > self.order:
                self.speed[0] = 1
                self.speed[1] *= 0
            if self.pos.right > 80:
                self.speed[0] = 0


numbers = []

for i in range(len(vector)):
    number = Number(i, vector[i])
    numbers.append(number)

while True:

    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()

    for number in numbers:
        screen.fill(black)

    if(counter == 10 and numbers[9].mov):
        if vt[9]:
            position[numbers[9].value % 10] -= 1
            numbers[9].order = position[numbers[9].value%10]
            vt[9] = False
        numbers[9].move('up position')

    for number in numbers:
        screen.blit(number.text, number.pos)

    for i in range(len(position)):
        a = myfont.render(str(i), False, (255, 255, 255))
        b = myfont.render(str(position[i]), False, (255, 255, 255))
        screen.blit(b, (20*i+10, height-30))
        screen.blit(a, (20*i+10, height-60))

    if calc < len(vector):
        arrow = myfont.render('<=', False, (255, 255, 255))
        screen.blit(arrow, (50, calc*30+10))
        position[vector[calc] % 10] += 1
        time.sleep(1)
        calc += 1

    pygame.display.update()
    pygame.time.delay(20)

    if calc == len(vector) and counter < len(position):
        position[counter] += position[counter-1]
        time.sleep(1)
        counter += 1
