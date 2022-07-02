#Precisa do sample.mp3 na mesma pasta do código

import playsound

playsound.playsound('sample.mp3')
playsound.wait()

import pygame

pygame.mixer.init()
pygame.mixer.music.load('sample.mp3')
pygame.mixer.music.play()