import tkinter as t

from PIL import Image,ImageTk

win=t.Tk()
win.geometry("500x400")
win.resizable(0,0)

img1=Image.open("photo1.jpg")
size=img1.resize((500,400))
final=ImageTk.PhotoImage(size)

lb = t.Label(win,image=final)
lb.place(x=0,y=0)
