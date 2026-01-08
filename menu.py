import pygame
import sys
import subprocess
import settings

pygame.init()

screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
pygame.display.set_caption(settings.TITLE)
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 48)

WHITE = (255, 255, 255)
GRAY = (60, 60, 60)
BLUE = (0, 200, 255)

def draw_button(text, x, y, w, h):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, GRAY, rect, border_radius=8)
    txt = font.render(text, True, WHITE)
    screen.blit(txt, (x + (w - txt.get_width()) // 2,
                      y + (h - txt.get_height()) // 2))
    return rect

def start_level(file):
    subprocess.Popen([sys.executable, file])

running = True
while running:
    clock.tick(settings.FPS)
    screen.fill(BLUE)

    btn1 = draw_button("Рівень 1", 250, 150, 300, 60)
    btn2 = draw_button("Рівень 2", 250, 240, 300, 60)
    btn3 = draw_button("Рівень 3", 250, 330, 300, 60)
    btn_exit = draw_button("Вийти", 250, 420, 300, 60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn1.collidepoint(event.pos):
                start_level(settings.LEVEL_1_FILE)

            if btn2.collidepoint(event.pos):
                start_level(settings.LEVEL_2_FILE)

            if btn3.collidepoint(event.pos):
                start_level(settings.LEVEL_3_FILE)

            if btn_exit.collidepoint(event.pos):
                running = False

    pygame.display.update()

pygame.quit()
sys.exit()
