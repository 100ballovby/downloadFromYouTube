from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('YouTube Video downloader')

title = Label(root, text='YouTube video downloader', font='Arial 20 bold')
title.pack()

link = StringVar()
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)


def download():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', fg='green').place(x=180, y=210)


btn = Button(root, text='Download', font='Arial 15 bold', padx=2, command=download)
btn.place(x=180, y=150)


if __name__ == '__main__':
    root.mainloop()