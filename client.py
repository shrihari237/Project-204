import socket
from threading import Thread
from tkinter import *
import random
from PIL import ImageTk

CLIENT = None
IP_ADDRESS = '127.0.0.1'
PORT = 5000

def setup():
    global CLIENT
    global PORT
    global IP_ADDRESS

    PORT  = 5000
    IP_ADDRESS = '127.0.0.1'

    CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    CLIENT.connect((IP_ADDRESS, PORT))

    # Creating First Window
    askName()

def askName():
    global playerName,nameEntry,nameWindow,canvas1

    nameWindow = Tk()
    nameWindow.title("Tambola Family Fun")
    nameWindow.geometry('800x600')

    screen_width = nameWindow.winfo_screenwidth()
    screen_height = nameWindow.winfo_screenheight()

    bg = ImageTk.PhotoImage(file = "./assets/background.png")

    canvas1 = Canvas(nameWindow,width = 500,height = 500)
    canvas1.pack(fill = 'both',expand = True)

    #Display image
    canvas1.create_image(0,0,image = bg,anchor = 'nw')
    canvas1.create_text(screen_width/4.5,screen_height/8,text ="Enter Name.",font=("Chalkboard SE",60),fill="black")

    nameEntry = Entry(nameWindow,width = 15,justify="center",font =("Chalkboard SE",30),bd=5,bg="white")
    nameEntry.place(x=screen_width/7,y=screen_height/5.5)

    button = Button(nameWindow,text="Save",font=("Chalkboard SE",30),width=11,command=saveName,height=2,bg="#80deea",bd=3)
    button.place(x=screen_width/6,y=screen_height/4)

    nameWindow.resizable(True,True)
    nameWindow.mainloop()

def saveName():
    global SERVER,playerName,nameWindow,nameEntry

    playerName = nameEntry.get()
    nameEntry.delete(0,END)
    nameWindow.destroy

    CLIENT.send(playerName.encode())

setup()    