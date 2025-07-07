#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
import pygame
pygame.mixer.init()
pygame.mixer.music.load('Ex021.mp3')
pygame.mixer.music.play()
input('\033[1;33mAperte Enter para parar a reprodução...\033[m')
pygame.mixer.music.stop()