#!/bin/python3

import pygame, pygame.sndarray
import numpy
import scipy.signal

sample_rate = 44100
pygame.mixer.pre_init(sample_rate, -16, 1)
pygame.init()

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

play_for(sine_wave(440, 4096), 1000)
