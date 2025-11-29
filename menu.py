import json
from pygame import*
import os
init()
window=display.set_mode((800,600))
window.fill((223, 196, 247))
clock=time.Clock()
game=True
#дані які зберагаємо в json
filename="settings.json"
levels=["легкий","середній","важкий"]
index=0

class Button():
    def __init__(self,x,y,width,height,text,color,text_color=(12, 7, 3)):
        self.rect=Rect(x,y,width,height)
        self.text=text
        self.color=color
        self.font = font.Font(None, 28)
        self.text_color=text_color
    def draw(self):
        draw.rect(window,self.color,self.rect)
        text_button=self.font.render(self.text,True,self.text_color)
        rect = text_button.get_rect(center=self.rect.center)
        window.blit(text_button,rect)
    def clicked(self,event):
        return event.type==MOUSEBUTTONDOWN and  self.rect.collidepoint(event.pos)
#кнопки
play=Button(200,80,200,50,"Грати",(105, 90, 74))
settings=Button(200,150,200,50,"Складність",(105, 90, 74))
exit_button=Button(200,220,200,50,"Вийти",(105, 90, 74))
while game:
    for e in event.get():
        if e.type==QUIT:
            game=False
    if play.clicked(e):
        print("Гра запускається")
    if settings.clicked(e):
        os.system("python settings.py")
        index=index+1%(len(levels))
        with open(filename, "w") as f:
               json.dump({"levels":levels[index]}, f)

    if exit_button.clicked(e):
        print("Вихід")
        game=False
    play.draw()
    settings.draw()
    exit_button.draw()
    
    display.update()
    clock.tick(60)
quit()
