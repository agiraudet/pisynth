#!/bin/python3

import pygame, pygame.sndarray
import numpy
import scipy.signal

sample_rate = 44100
pygame.mixer.pre_init(sample_rate, -16, 1)
pygame.init()
(wd, hg) = (500, 100)
win = pygame.display.set_mode((wd, hg))
pygame.display.set_caption('test')

def play_for(sample_wav, ms):
    sound = pygame.sndarray.make_sound(sample_wav)
    sound.play(-1)
    pygame.time.delay(ms)
    sound.stop()

def sine_wave(hz, peak, n_samples=sample_rate):
    len = sample_rate / float(hz)
    omega = numpy.pi * 2 / len
    xvalues = numpy.arange(int(len)) * omega
    onecycle = peak * numpy.sin(xvalues)
    return numpy.resize(onecycle, (n_samples,)).astype(numpy.int16)

class Key():
    def __init__(self, x, y, wd, hg, num):
        self.num = num
        self.rect = pygame.Rect(x, y, wd, hg)

    def draw(self, win, color):
        pygame.draw.rect(win, color, self.rect)
        pygame.draw.rect(win, (0,0,0), self.rect, width=1)

    def clic_in(self):
        (x,y) = pygame.mouse.get_pos()
        if x >= self.rect.x and x <= self.rect.x + self.rect.width:
            if y >= self.rect.y and y <= self.rect.y + self.rect.height:
                return 1
        return 0

key_nb = 20
key_size = wd / key_nb
keys = []
i = 0
n = 0
while i < wd:
    key = Key(i,0, key_size, hg, n)
    keys.append(key)
    i+= key_size
    n += 1

loop = True
while loop:
    for k in keys:
        k.draw(win, (255,255,255))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    clic = pygame.mouse.get_pressed()
    if clic[0]:
        for k in keys:
            if k.clic_in():
                k.draw(win, (0,255,0))
                pygame.display.update()
                play_for(sine_wave(k.num * 100, 4096), 500)
