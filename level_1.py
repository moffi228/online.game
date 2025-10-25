from pygame import*
from random import randint
from math import hypot
init()
window=display.set_mode((800,600))
display.set_caption('Agar.io')

window.fill((205, 227, 233))
clock=time.Clock()

my_player=[0,0,20]
all_players=[]

class Food():
    def __init__(self,x,y,r,c):
        self.x=x
        self.y=y
        self.radius=r
        self.color=c
    def check_collision(self,player_x,player_y,player_r):
        dx=self.x - player_x
        dy=self.y - player_y
        return hypot(dx, dy) <= self.radius + player_r

eats=[]
for i in range(30):
    eats.append(Food(randint(0,800),randint(0,600),10,(randint(0,255),randint(0,255),randint(0,255))))

running=True
while running:
    window.fill((205, 227, 233))
    scale=max(0.3, min(50 / my_player[2], 1.5))

    to_remove=[]

    for e in event.get():
        if e.type==QUIT:
            quit()
    window.fill((205, 227, 233))
    for food in eats:
        draw.circle(window,food.color,(food.x,food.y),food.radius)
        if food.check_collision(my_player[0],my_player[1],my_player[2]):
            my_player[2] += int(food.radius * 0.2)
            to_remove.append(food)
            eats.remove(food)
    draw.circle(window,(211, 105, 233),(my_player[0],my_player[1]), my_player[2])
    keys = key.get_pressed()
    if keys[K_w]:my_player[1] -= 15
    if keys[K_s]:my_player[1] += 15
    if keys[K_a]:my_player[0] -= 15
    if keys[K_d]:my_player[0] += 15

    display.update()
    clock.tick(60)
