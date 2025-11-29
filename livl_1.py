from pygame import*
from random import randint
from math import hypot
init()
window=display.set_mode((800,600))
display.set_caption('Online_GAame')
mixer_music.load("retro-arcade-game-music-396890.mp3")
mixer_music.play()

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
        dx=self.x-player_x
        dy=self.y-player_y
        return hypot (dx,dy)<=self.radius+player_r
        
font=font.Font(None,40)
score=0
text=font.render(f"Знищино:{score}",True,(141, 223, 0)) 
hp=10
text2=font.render(f"Здоров'я:{hp}",True,(141, 223, 0))     
eats=[]
for i in range(30):
    eats.append(Food(randint(0,800),randint(0,600),10,(randint(0,255),randint(0,255),randint(0,255)))) 

running=True
while running: 
    
    window.fill((205, 227, 233)) 
    window.blit(text,(500,0))
    window.blit(text2,(500,20))
    scale=max(0.3, min(50 / my_player[2], 1.5))  
    to_remove=[]     
    for e in event.get():
        if e.type==QUIT:
            running=False
    draw.circle(window,(211, 105, 233),(my_player[0],my_player[1]),my_player[2])
    keys=key.get_pressed()
    if keys[K_w]:my_player[1] -= 15
    if keys[K_s]:my_player[1]+=15
    if keys[K_a]:my_player[0]-=15
    if keys[K_d]:my_player[0]+=15
    for food in eats:
        draw.circle(window, food.color, (food.x, food.y), food.radius)
        if food.check_collision(my_player[0],my_player[1],my_player[2]):
             my_player[2] += int(food.radius * 0.2)
             to_remove.append(food)
             eats.remove(food) 
             score+=1
             text=font.render(f"Знищино:{score}",True,(141, 223, 0)) 
             hp+=2
             text2=font.render(f"Здоров'я:{hp}",True,(141, 223, 0))  
        else:
           sx = int((food.x - my_player[0]) * scale + 500)
           sy = int((food.y - my_player[1]) * scale + 500)
           draw.circle(window, food.color, (sx, sy), int(food.radius * scale))
    display.update()
    clock.tick(60)
quit()         
