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
def load_image(name, size=None):
    image = pygame.image.load(name)
    if size:
        image = pygame.transform.scale(image, size)
    return image.convert_alpha() if name.endswith('.png') else image.convert()


def draw_text(text, x, y, font, color=BLACK):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))


def draw_button(text, x, y, width, height, font):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, BLACK, rect, 2)
    label = font.render(text, True, BLACK)
    text_rect = label.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(label, text_rect)
    return rect

    def load_highscore():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as f:
            return int(f.read().strip())
    return 0


def save_highscore(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

        class DinoGame:
    def __init__(self):
        self.dino_img = load_image("dino.png", (DINO_WIDTH, DINO_HEIGHT))
        self.cactus_img = load_image("cactus.png", (CACTUS_WIDTH, CACTUS_HEIGHT))
        self.font = pygame.font.Font(None, 48)
        self.font_large = pygame.font.Font(None, 72)
        self.reset_game()
        self.paused = False

        # Цвета фона
        self.day_color = (135, 206, 235)   # Голубой
        self.night_color = (10, 10, 40)    # Тёмно-синий