import pygame
from time import sleep

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('sevalente.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    sleep(1)

