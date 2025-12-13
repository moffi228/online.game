from pygame import*
import sounddevice as sd
fs = 44100
chunk = 1024
width, height = 800, 400
init()
window = display.set_mode((width, height))
clock = time.Clock()
data=[0,0]*chunk
class Button():
    def __init__(self, x, y, width, height, text_color, hover_color,font,color,text):
        self.rect = Rect(x, y, width, height)
        self.text = text
        self.hover_color = hover_color
        self.font = font
        self.text_color = text_color
        self.color = color

    def draw(self, screen):
        mouse_pos = mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            draw.rect(screen, self.hover_color, self.rect)
        else:
            draw.rect(screen, self.color, self.rect)
        text=self.font.render(self.text, True, self.text_color)
        text_rect=text.get_rect(center=self.rect.center)
        screen.blit(text, text_rect)
    def clicked(self,event):
        if e.type ==MOUSEBUTTONDOWN and event.button==1:
                if self.rect.collidepoint(event.pos):
                    return True
        return False
font=font.Font(None, 36)
button=Button(400, 200, 100, 60,(26, 54, 216),(238, 202, 216),font,(0,0,100),"Start")
while True:
    for e in event.get():
        if e.type==QUIT:
            runnig=False
            quit()
            
        if button.clicked(e):
            print("Recording...")

    window.fill((30,30,30))
    button.draw(window)

    display.update()
    clock.tick(60)

quit()
