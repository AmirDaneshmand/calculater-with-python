import tkinter as tk
from compress_module import compress, decompress
from tkinter import filedialog

def compression(i, o):
    compress(i, o)
    
def open_file():
    filename = filedialog.askopenfilename(initialdir='/Cmpression/', title="Select a file to compress")
    return filename

window = tk.Tk()
window.title("COmpression engine")
window.geometry("600x400")



compress_button = tk.Button(window, text="Compress", command=lambda:compression(open_file(),"compressedOutput.txt"))

compress_button.grid(row=2, column=1)

window.mainloop()