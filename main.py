import pygame
import random
import os # Проверка

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
    pygame.draw.rect(screen, BLACK, rect, width=2, border_radius=8)
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
            def draw(self):
        # Чередование фона по счёту
        phase = (self.score // 30) % 2
        if phase == 0:
            screen.fill(self.day_color)
        else:
            screen.fill(self.night_color)

        # Анимация фона (для песка и препятствий)
        for i in range(2):
            self.bg_x[i] -= self.speed // 2
            if self.bg_x[i] <= -WIDTH:
                self.bg_x[i] = WIDTH

        # Песок
        pygame.draw.rect(screen, SAND_COLOR, (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))

        # Кактусы
        for group in self.obstacles:
            for cactus in group:
                screen.blit(self.cactus_img, (cactus.x, cactus.y))
                    # Дино
                    # screen.blit(self.dino_img, ...)
pygame.draw.ellipse(screen, (50, 50, 50), 
                    (self.dino.x + 10, self.dino.y + DINO_HEIGHT - 5, 
                     DINO_WIDTH - 20, 5))
        screen.blit(self.dino_img, (self.dino.x, self.dino.y))

        # Счёт и режим
        draw_text(f"СЧЁТ: {self.score}", 20, 20, self.font)
        mode = "АВТО: ВКЛ (Q)" if self.auto_jump else "АВТО: ВЫКЛ (Q)"
        draw_text(mode, WIDTH - 320, 20, self.font)

        # Пауза
        if self.paused:
            pause_text = self.font_large.render("ПАУЗА", True, BLACK)
            screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2))

            def run(self):
        running = True
        while running:
            running = self.handle_events()
            running = running and self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        return self.score 

        def main_menu():
    game = DinoGame()
    highscore = load_highscore()

    while True:
        screen.fill(game.day_color)
        title = game.font_large.render("Dino", True, BLACK)
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 4))

        start_btn = draw_button("Начать игру", WIDTH // 2 - 100, HEIGHT // 2, 200, 60, game.font)
        records_btn = draw_button("Рекорды", WIDTH // 2 - 100, HEIGHT // 2 + 80, 200, 60, game.font)
small_font = pygame.font.Font(None, 36)
hint = small_font.render("Пробел — прыжок | Q — авто | P — пауза", True, BLACK)
screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, HEIGHT - 50))

        pygame.display.flip()

            for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.collidepoint(event.pos):
                    score = game.run()
                    if score > highscore:
                        highscore = score
                        save_highscore(highscore)
                    if not game_over_menu(score, highscore, game.font, game.font_large):
                        return
                    game.reset_game()
                if records_btn.collidepoint(event.pos):
                    show_records(highscore, game.font, game.font_large)
                def game_over_menu(score, highscore, font, font_large):
    while True:
        screen.fill((135, 206, 235))  # Голубой фон меню

        score_text = f"ВАШ СЧЁТ: {score}"
        highscore_text = f"РЕКОРД: {highscore}"

        score_surface = font_large.render(score_text, True, BLACK)
        highscore_surface = font_large.render(highscore_text, True, BLACK)

        screen.blit(score_surface, (WIDTH // 2 - score_surface.get_width() // 2, HEIGHT // 4))
        screen.blit(highscore_surface, (WIDTH // 2 - highscore_surface.get_width() // 2, HEIGHT // 4 + 80))

        restart_btn = draw_button("ЕЩЁ РАЗ", WIDTH // 2 - 120, HEIGHT // 2 + 100, 240, 70, font)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN and restart_btn.collidepoint(event.pos):
                return True
        def show_records(highscore, font, font_large):
    while True:
        screen.fill((135, 206, 235))
        draw_text("РЕКОРДЫ", WIDTH // 2 - 100, HEIGHT // 4, font_large)
        draw_text(f"ЛУЧШИЙ: {highscore}", WIDTH // 2 - 100, HEIGHT // 3, font)

        back_btn = draw_button("НАЗАД", WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 60, font)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and back_btn.collidepoint(event.pos):
                return 
            if __name__ == "__main__":
            main_menu()                     