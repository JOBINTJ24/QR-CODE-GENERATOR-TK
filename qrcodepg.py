from os import link
from  tkinter import *
import pyqrcode


#import pillow
from  PIL import ImageTk,Image
root=Tk()

def generate():
    link_name=name_entry.get()
    link=link_entry.get()
    file_name=link_name + ".png"
    url=pyqrcode.create(link)
    url.png(file_name,scale=8)
    image=ImageTk.PhotoImage(Image.open(file_name))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(200,450,window=image_label)


canvas=Canvas(root,width=400,height=600)
canvas.pack()
can_label=Label(root,text="QR CODE GENERATOR",fg="blue",font=("Arial",30))
canvas.create_window(150,50,window=can_label)
name_label=Label(root,text="Link name")
link_label=Label(root,text="Link")

canvas.create_window(200,100,window=name_label)
canvas.create_window(200,160,window=link_label)

name_entry=Entry(root)
link_entry=Entry(root)

canvas.create_window(200,130,window=name_entry)
canvas.create_window(200,180,window=link_entry)

button=Button(text="Generate QR Code",command=generate)
canvas.create_window(200,230,window=button)








root.mainloop()