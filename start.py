from pygame import*
from random import randint
init()
window=display.set_mode((1000,800))
clock = time.Clock()
class Player():
    def __init__(self,x,y,width,height,images):
       self.images = [transform.scale(image.load(img), (width, height)) for img in images]
       self.frame_index = 0
       self.image_speed = 0.05  # Швидкість анімації
       self.rect = self.images[0].get_rect(topleft=(x, y))
       self.current_img = self.images[0]

    def reset(self):
        window.blit(self.current_img,(self.rect.x,self.rect.y))
    def animate(self):
         self.frame_index += self.image_speed
         if self.frame_index >= len(self.images):
           self.frame_index = 0
         self.current_img = self.images[int(self.frame_index)]
player_img=[f'{i}.png' for i in range(1,3)]
player=Player(400,150,180,200,player_img)
btn=Rect(375,350,350,100)
font=font.Font(None,40)
player_text=font.render("Play",True,(255, 169, 0))
wait=0
while True:
    for e in event.get():
        if e.type==QUIT:
            quit()
    window.fill((255, 169, 197))
    player.reset()
    player.animate()
    if wait==0:
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        wait=20
    else:
        wait=-1
    draw.rect(window,(r,g,b),btn,border_radius=20)
    draw.rect(window, (200, 200, 200), [btn.x, btn.y, btn.w, btn.h], 6, border_radius=15)
    window.blit(player_text, (btn.x+120, btn.y+20))

    display.update()
    clock.tick(60)
