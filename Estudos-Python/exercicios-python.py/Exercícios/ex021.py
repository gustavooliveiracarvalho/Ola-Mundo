"""Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo
 MP3."""

import pygame
pygame.init()
pygame.mixer.music.load('ex021-deca-musica.mp3')
pygame.music.play()
pygame.event.wait()
