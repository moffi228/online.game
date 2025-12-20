from pygame import*
init()
import socket
from PIL import Image

mixer_music.load("Elektronika_60_-_Melodiya_iz_Tetrisa_(SkySound.cc).mp3")
mixer_music.play()
window = display.set_mode((500, 500))
clock = time.Clock()
display.set_caption("LEVEL 2")
window.fill((0, 0, 0))

# Завантаження зображень
player_img = image.load("завантаження1.png")
player_img = transform.scale(player_img, (20, 100))

player2_img = image.load("завантаження.png")
player2_img = transform.scale(player2_img, (20, 100))

wall_img = image.load("завантаження (5).jpg")
wall_img = transform.scale(wall_img, (500, 20))

wall2_img = image.load("завантаження (5) copy.jpg")
wall2_img = transform.scale(wall2_img, (500, 20))

ball_img = image.load("завантаження (3).jpg")
ball_img = transform.scale(ball_img, (20, 20))

# Створюємо Rect для гравців і м'яча
player1 = player_img.get_rect()
player1.x = 1
player1.y = 200

player2 = player2_img.get_rect()
player2.x = 479
player2.y = 200

wall_1= wall_img.get_rect()
wall_1.x = 0
wall_1.y = 0

wall_2 = wall2_img.get_rect()
wall_2.x = 0
wall_2.y = 480

ball = ball_img.get_rect()
ball.x = 250
ball.y = 250

# Шрифти
font_win = font.Font(None, 72)
font_main = font.Font(None, 56)

score_player1 = 0
score_player2 = 0
text= font_main.render(f"{score_player1} : {score_player2}", True, (0, 0, 0))
def update_1():

    keys = key.get_pressed()
    if keys[K_w]:
        player1.y -= 10
    if keys[K_s]:
        player1.y += 10

def update_2():
    keys = key.get_pressed()
    if keys[K_UP]:
        player2.y -= 10
    if keys[K_DOWN]:
        player2.y += 10 
ball_speed_x = 5
ball_speed_y = 5

def collision():
    global ball_speed_x
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x*= -1
    
    global wall_1, wall_2
    if player1.colliderect(wall_1) or player1.colliderect(wall_2):
        if player1.colliderect(wall_1):
            player1.y = wall_1.y + wall_1.height
        if player1.colliderect(wall_2):
            player1.y = wall_2.y - player1.height
    if player2.colliderect(wall_1) or player2.colliderect(wall_2):
        if player2.colliderect(wall_1):
            player2.y = wall_1.y + wall_1.height
        if player2.colliderect(wall_2):
            player2.y = wall_2.y - player2.height

def move_ball():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.y <= 0 or ball.y + ball.height >= 500:
        ball_speed_y *= -1

    if ball.x <= 0 or ball.x + ball.width >= 500:
        ball_speed_x *= -1
def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.center =(250,250)
    ball_speed_x *= -1
def score():
    global score_player1, score_player2
    if ball.x <=0:
        score_player2 +=1
        reset_ball()
    elif ball.x+ball.width>=500:
        score_player1 +=1
        reset_ball()
# Гра   
while True:
    for e in event.get():
        if e.type == QUIT:
            quit()

    # Рух гравця 1
    update_1()
    update_2()
    move_ball()
    collision()
    score()
    # Малювання
    window.fill((255, 255, 255))
    window.blit(player_img, player1)
    window.blit(player2_img, player2)
    window.blit(ball_img, ball)
    window.blit(wall_img, wall_1)
    window.blit(wall2_img, wall_2)
    text= font_main.render(f"{score_player1} : {score_player2}", True, (0, 0, 0))
    window.blit(text, (200, 20))
    # Оновлення екрану
    display.update()
    clock.tick(60)

