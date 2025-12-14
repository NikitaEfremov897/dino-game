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

            def reset_game(self):
        self.dino = pygame.Rect(100, GROUND_Y - DINO_HEIGHT, DINO_WIDTH, DINO_HEIGHT)
        self.velocity = 0
        self.speed = 6
        self.last_obstacle_x = WIDTH
        self.next_cactus_distance = random.randint(400, 800)
        self.obstacles = [self.generate_obstacles()]
        self.score = 0
        self.auto_jump = False
        self.clock = pygame.time.Clock()
        self.jump_power = -22.5
        self.gravity = 1.5
        self.max_speed = 10
        self.speed_interval = 12
        self.speed_increase = 0.2
        self.bg_x = [0, WIDTH]

        # Для двойного прыжка
        self.on_ground = True
        self.double_jump_used = False

            def generate_obstacles(self):
        num = random.choices([1, 2, 3], [0.6, 0.3, 0.1])[0]
        return [pygame.Rect(self.last_obstacle_x + i * 20, GROUND_Y - CACTUS_HEIGHT,
                            CACTUS_WIDTH, CACTUS_HEIGHT) for i in range(num)]

         def should_jump(self):
        for group in self.obstacles:
            for cactus in group:
                distance = cactus.x - (self.dino.x + DINO_WIDTH)
                if (JUMP_DISTANCE_MIN <= distance <= JUMP_DISTANCE_MAX and
                        self.dino.y >= GROUND_Y - DINO_HEIGHT):
                    return True
        return False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.on_ground:
                        self.velocity = self.jump_power
                        self.on_ground = False
                    elif not self.double_jump_used:
                        self.velocity = self.jump_power
                        self.double_jump_used = True
                if event.key == pygame.K_q:
                    self.auto_jump = not self.auto_jump
                if event.key == pygame.K_p:  # Пауза
                    self.paused = not self.paused
        return True

            def update(self):
        if self.paused:
            return True

        if self.auto_jump and self.should_jump() and self.dino.y >= GROUND_Y - DINO_HEIGHT:
            if self.on_ground:
                self.velocity = self.jump_power
                self.on_ground = False
            elif not self.double_jump_used:
                self.velocity = self.jump_power
                self.double_jump_used = True

        self.velocity += self.gravity
        self.dino.y += self.velocity

        if self.dino.y >= GROUND_Y - DINO_HEIGHT:
            self.dino.y = GROUND_Y - DINO_HEIGHT
            self.velocity = 0
            self.on_ground = True
            self.double_jump_used = False

        for group in self.obstacles:
            for cactus in group:
                cactus.x -= self.speed

                if self.obstacles[-1][0].x < WIDTH - self.next_cactus_distance:
            group = self.generate_obstacles()
            self.obstacles.append(group)
            self.last_obstacle_x = group[-1].x
            self.next_cactus_distance = random.randint(400, 800)

        if self.obstacles[0][0].x < -CACTUS_WIDTH:
            self.obstacles.pop(0)
            self.score += 1
            if self.score % self.speed_interval == 0 and self.speed < self.max_speed:
                self.speed += self.speed_increase

        return not any(self.dino.collidelist(group) >= 0 for group in self.obstacles)                       