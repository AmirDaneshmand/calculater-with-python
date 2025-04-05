from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil

def download():
    video_path = url_entry.get()
    file_path = path_label.cget("text")
    print("downloading ...")
    mp4 = YouTube(video_path).streams.get_highest_resolution().download()
    video_clip = VideoClip(mp4)
    
    # code for mp3
    audio_file = video_clip.audio
    audio_file.write_audiofile('audio.mp3')
    audio_file.close()
    shutil.move('audio.mp3', file_path)
    # code for mp3
    
    video_clip.close()
    shutil.move(mp4, file_path)
    print("download complete")

def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

root = Tk()
root.title('Video Downloader')
canvas = Canvas(root, width=400, height=500)
canvas.pack()

app_lable = Label(root, text="Video Downloader", fg='blue', font=("Arial", 30))
canvas.create_window(200, 20, window=app_lable)

url_label = Label(root, text="Enter video URL")
url_entry = Entry(root)
canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)

path_label = Label(root, text="Select path to download")
path_button = Button(root, text="Select", command=get_path)
canvas.create_window(200, 150, window=path_label)
canvas.create_window(200, 180, window=path_button)

download_button = Button(root, text='Download')
canvas.create_window(200, 250, window=download_button)


root.mainloop()
