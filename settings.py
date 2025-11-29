from customtkinter import*
window=CTk()
window.geometry("400x400")
import os
def easy_level():
    os.system("python livl1.py")

easy=CTkButton(window, command=easy_level, width=200,height=100, text="Легкий", border_color="black", border_width=2, hover_color="green")
easy.place(x=120, y=30)
def medium_level():
    os.system("python lvel2.py")

medium=CTkButton(window, command=medium_level, width=200, height=100, text="Середній", border_color="black", border_width=2, hover_color="green")
medium.place(x=120, y=150) 

hard=CTkButton(window, width=200, height=100, text="Тяжкий", border_color="black", border_width=2, hover_color="green")
hard.place(x=120,y=270)
window.mainloop()