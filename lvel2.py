from pygame import*
init()
import socket
from PIL import Image

window = display.set_mode((500, 500))
clock = time.Clock()
display.set_caption("LEVEL 2")
window.fill((0, 0, 0))

# Завантаження зображень
player_img = image.load("завантаження1.png")
player_img = transform.scale(player_img, (50, 100))

player2_img = image.load("завантаження.png")
player2_img = transform.scale(player2_img, (50, 100))

ball_img = image.load("завантаження (3).jpg")
ball_img = transform.scale(ball_img, (20, 20))

# Створюємо Rect для гравців і м'яча
player1 = player_img.get_rect()
player1.x = 0
player1.y = 200

player2 = player2_img.get_rect()
player2.x = 450
player2.y = 200

ball = ball_img.get_rect()
ball.x = 250
ball.y = 250

# Шрифти
font_win = font.Font(None, 72)
font_main = font.Font(None, 56)

score_player1 = 0
score_player2 = 0

def update_1():
    keys = key.get_pressed()
    if keys[K_w]:
        player1.y -= 10
    if keys[K_s]:
        player1.y += 10

# Гра
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()

    # Рух гравця 1
    update_1()

    # Малювання
    window.fill((255, 255, 255))
    window.blit(player_img, player1)
    window.blit(player2_img, player2)
    window.blit(ball_img, ball)

    # Оновлення екрану
    display.update()
    clock.tick(40)
