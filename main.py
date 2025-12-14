import pygame
import random
import os

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 1200, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SAND_COLOR = (194, 178, 128)
GROUND_Y = HEIGHT - 100
DINO_WIDTH, DINO_HEIGHT = 60, 60
CACTUS_WIDTH, CACTUS_HEIGHT = 30, 50
JUMP_DISTANCE_MIN = 15
JUMP_DISTANCE_MAX = 30

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino")