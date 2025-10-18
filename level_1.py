from pygame import*
from random import randint
init()
window=display.set_mode((800,800))
display.set_caption('Agar.io')

window.fill((255, 165, 0))
clock=time.Clock()

my_player=[0,0,20]
all_players=[]

class Food():
    def __init__(self,x,y,r,c):
        self.x=x
        self.y=y
        self.radius=r
        self.color=c

eats=[Food(randint(0,800),randint(0,600),10,(randint(0,255),randint(0,255),randint(0,255)))]


while True:
    for e in event.get():
        if e.type==QUIT:
            False
    draw.circle(window,(255, 0, 0), (500,500), my_player[2])
    keys = key.get_pressed()
    if keys[K_w]:my_player[1] -= 15
    if keys[K_s]:my_player[1] += 15
    if keys[K_a]:my_player[0] -= 15
    if keys[K_d]:my_player[0] += 15

    display.update()
    clock.tick(60)
