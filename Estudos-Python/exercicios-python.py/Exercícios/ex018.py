"""Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o
valor do seno, cosseno e tangente desse ângulo."""

from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo: '))

radian = radians(angulo)

seno = sin(radian)
cosseno = cos(radian)
tangente = tan(radian)

print(f'O ângulo de {angulo} tem as medidas:\n Seno: {seno:.2f}\n Cosseno: {cosseno:.2f}\n Tangente: {tangente:.2f}')

