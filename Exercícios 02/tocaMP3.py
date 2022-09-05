# tocando música no python
import pygame

pygame.mixer.init()
pygame.mixer.music.load('nomedamusica.MP3')
pygame.mixer.music.play()
input()
pygame.event.wait()
