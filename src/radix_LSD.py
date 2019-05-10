import sys
import time
import random
import pygame
from pygame.locals import *


pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

calc = 0
counter = 1


vector = [0]*10

for i in range(len(vector)):
    vector[i] = random.randint(0, 1000)

n_max = vector[0]

for i in range(1, len(vector)):
    if n_max < vector[i]:
        n_max = vector[i]

n_max = len(str(n_max))
ten_pow = 1

p_vector = len(vector) - 1

vt = ['true']*len(vector)
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
                self.speed[1] = 0
            if self.pos.right > 200:
                self.speed[0] = -1
                self.mov = False

        if go == 'down position' and self.mov:
            self.pos = self.pos.move(self.speed)
            if self.pos.right == 100:
                self.speed[0] = 0
                self.speed[1] = 1
            if self.pos.top > self.order*30+10:
                self.speed[0] = 1
                self.speed[1] = 0
            if self.pos.right > 200:
                self.speed[0] = -1
                self.mov = False

        if go == 'back position' and not self.mov:
            self.pos = self.pos.move(self.speed)
            if self.pos.left < 10:
                self.speed[0] = 1
                self.mov = True


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

    if p_vector < 0:
        for number in numbers:
            number.move('back position')

        if numbers[len(numbers)-1].mov and ten_pow < n_max:
            ten_pow += 1
            calc = 0
            counter = 1
            vt = ['true']*len(vector)
            position = [0]*10

            for number in numbers:
                vector[number.order] = number.value

            p_vector = len(vector) - 1
            numbers = []

            for i in range(len(vector)):
                number = Number(i, vector[i])
                numbers.append(number)

    elif(counter == 10 and numbers[p_vector].mov):
        if vt[p_vector] == 'true':
            position[(numbers[p_vector].value %
                      10**ten_pow)//10**(ten_pow - 1)] -= 1
            if numbers[p_vector].order > position[(numbers[p_vector].value % 10**ten_pow)//10**(ten_pow - 1)]:
                vt[p_vector] = 'up position'
            else:
                vt[p_vector] = 'down position'
            numbers[p_vector].order = position[(
                numbers[p_vector].value % 10**ten_pow)//10**(ten_pow - 1)]
        numbers[p_vector].move(vt[p_vector])

    elif(counter == 10 and not numbers[p_vector].mov):
        p_vector -= 1

    for number in numbers:
        screen.blit(number.text, number.pos)

    for i in range(len(position)):
        a = myfont.render(str(i), False, (255, 255, 255))
        b = myfont.render(str(position[i]), False, (255, 255, 255))
        screen.blit(b, (70*i+10, height-30))
        screen.blit(a, (70*i+10, height-60))

    if calc < len(vector):
        arrow = myfont.render('<=', False, (255, 255, 255))
        screen.blit(arrow, (50, calc*30+10))
        position[(vector[calc] % 10**ten_pow)//10**(ten_pow - 1)] += 1
        time.sleep(1)
        calc += 1

    pygame.display.update()
    pygame.time.delay(5)

    if calc == len(vector) and counter < len(position):
        position[counter] += position[counter-1]
        time.sleep(1)
        counter += 1
