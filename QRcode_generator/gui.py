from PIL import Image as PilImage, ImageTk
from tkinter import *
import pyqrcode

def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)
    image = ImageTk.PhotoImage(PilImage.open(file_name))  # تغییر Image به PilImage
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200, 450, window=image_label)

root = Tk()

canvas = Canvas(root, width=400, height=600)
canvas.pack()

app_label = Label(root, text="QR Code Generator", fg='blue', font=("Arial", 30))
canvas.create_window(200, 50, window=app_label)

name_label = Label(root, text="Link name")
link_label = Label(root, text="Link")
canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

buttom = Button(root, text="Generate", command=generate)
canvas.create_window(200, 230, window=buttom)

root.mainloop()
