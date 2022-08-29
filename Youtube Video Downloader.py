from email.mime import image
from importlib.resources import path
import io
from logging import root
from subprocess import CREATE_NO_WINDOW
from this import s
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from turtle import left
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil
import os
from PIL import Image,ImageTk
from io import BytesIO
from urllib.request import Request, urlopen
import tkinter as tk





#functions


def select_path():
    path=filedialog.askdirectory()#allows the path selection
    path_label.config(text=path)


#downlaod function
def download_video_file():
    screen.title("Downloading...")
    yt=YouTube(link_field.get())
    user_path=path_label.cget("text")#gets the selectd path
    video=yt.streams.get_highest_resolution().download()#gets the highest resolution video
    vid_clip=VideoFileClip(video)
    vid_clip.close()
    shutil.move(video, user_path)
    screen.title("Download finished")

def download_audio_file():
    yt=YouTube(link_field.get())
    user_path=path_label.cget("text")
    screen.title("Downloading...")
    video=yt.streams.filter(only_audio=True).first()
    out_file=video.download(output_path=user_path)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    screen.title("Download Finished")

def check_details():
    yt=YouTube(link_field.get())
    canvas.create_text(22,280,text="Title:",font=("Bold",10),anchor="center")
    canvas.create_text(40,280,text=yt.title,font=('Arial',9),anchor="w",width=450)
    canvas.create_text(25,320,text="Views:",font=("Bold",10))
    canvas.create_text(50,320,text=yt.views,font=('Arial',9),anchor="w")
    canvas.create_text(25,360,text="Author:",font=("Bold",10))
    canvas.create_text(50,360,text=yt.author,font=('Arial',9),anchor="w")
    imageurl=yt.thumbnail_url
    raw_data=urlopen(imageurl).read()
    im=Image.open(BytesIO(raw_data))
    resize=im.resize((300,200), Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(resize)
    label=tk.Label(image=photo)
    label.image =photo
    label.place(x=500,y=400,anchor="e")
    

    



#canvas
screen=Tk()
title=screen.title('Youtube Downloader by Avijit')
canvas = Canvas(screen, width=500,height=500)
canvas.pack()


#logo
logo_img=PhotoImage(file='ytlogo.png')
logo_img=logo_img.subsample(3,3)


#adding the logo to the canvas
canvas.create_image(250, 40, image = logo_img)

#link input
link_field=Entry(screen,width=50)
link_label= Label(screen,text="Enter Download Link",font=('Arial',15))


#downloading path
path_label=Label(screen,text="Select Path For Download",font=('Arial',10))
select_btn=Button(screen,text="Select",command=select_path,bg="gray")


#adding the link entering part and the downloading part in the canvas
canvas.create_window(250,100,window=link_label)
canvas.create_window(250,130,window=link_field)
canvas.create_window(250,160,window=path_label)
canvas.create_window(250,190,window=select_btn)



#download th actual video
download_btn1= Button(screen, text='Download video File',font="Bold", command=download_video_file,bg="gray")
canvas.create_window (420,230,window=download_btn1)
download_btn2= Button(screen, text='Download audio File', font="Bold",command=download_audio_file,bg="gray")
canvas.create_window (230,230,window=download_btn2)
download_btn3= Button(screen, text='Check Details', font="Bold",command=check_details,bg="gray")
canvas.create_window (65,230,window=download_btn3)



canvas.create_text(5,470,text="ENCODED BY",font=("Matura MT Script Capitals",13),anchor="w",width=180)
canvas.create_text(45,490,text="AVIJIT BHUIN",font=("Ink Free",14),anchor="w",width=150)


screen.mainloop()