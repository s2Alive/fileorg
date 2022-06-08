#imports
from logging import root
from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter
import pygame
import os
import tkinter as tk


#criando a janela
root = Tk()
root.title('Organizador de pastas ainda não funcional')
root.geometry('693x560')
root.config(bg='black')
root.resizable(False, False)

#adicionando a img
img = PhotoImage(file="capa.png")
label = Label(root,image=img)
label.place(x=0, y=0)

#funções
def directory():
    # get a directory path by user
    filepath=filedialog.askdirectory(title="Selecione a pasta")
    print (filepath)

#TESTE DE BOLEANO

def isChecked():
    return print("Checkbutton is checked:{}".format(check1.get()))


#checkbutton

check1 = BooleanVar()
check2 = BooleanVar()
check3 = BooleanVar()
check4 = BooleanVar()
check5 = BooleanVar()
check6 = BooleanVar()


#labels e buttons
text1 = Label(root, bg = "white", height=3, width=20, text="Organizador de pastas")
text1.place(x=270, y=50)

text2 = Label(root, bg = "white", height=3, width=20, text="Selecione a pasta")
text2.place(x=270, y=150)

folderbutton = Button(root, bg = "white",text='Procurar',relief=RAISED,font=('Arial Bold', 12), command = directory)
folderbutton.place(x=300, y=220)

text3 = Label(root, bg = "white", height=3, width=30, text="Selecione o tipo dos arquivos:")
text3.place(x=230, y=280)

checkbutton1 = Checkbutton (root, bg = "white", activebackground = "blue", text="Power Point", var=check1, onvalue=True, offvalue=False, command=isChecked)
checkbutton1.place(x=370, y=350)


checkbutton2 = Checkbutton (root, bg = "white",activebackground = "blue", text="Excel", var=check2, onvalue=True, offvalue=False)
checkbutton2.place(x=310, y=350)

checkbutton3 = Checkbutton (root, bg = "white",activebackground = "blue", text="Texto", var=check3, onvalue=True, offvalue=False)
checkbutton3.place(x=230, y=350)

checkbutton4 = Checkbutton (root, bg = "white",activebackground = "blue", text="Word", var=check4, onvalue=True, offvalue=False)
checkbutton4.place(x=370, y=400)

checkbutton5 = Checkbutton (root, bg = "white",activebackground = "blue", text="PDF", var=check5, onvalue=True, offvalue=False)
checkbutton5.place(x=310, y=400)

checkbutton6 = Checkbutton (root, bg = "white",activebackground = "blue", text="Imagens", var=check6, onvalue=True, offvalue=False)
checkbutton6.place(x=230, y=400)

button = Button(root, bg = "white",text='Organizar pasta',relief=RAISED,font=('Arial Bold', 12))
button.place(x=290, y=480)

# PLAYER DE MUSICA DAQUI PRA BAIXO ################################################################

# Defining MusicPlayer Class
class MusicPlayer:

  # Defining Constructor
  def __init__(self,root):
    self.root = root
    # Title of the window
    self.root.title("Organizador de pastas ainda não funcional")
    # Initiating Pygame
    pygame.init()
    # Initiating Pygame Mixer
    pygame.mixer.init()
    # Declaring track Variable
    self.track = StringVar()
    # Declaring Status Variable
    self.status = StringVar()

    # Creating Track Frame for Song label & status label
    trackframe = LabelFrame(self.root,text="",bg="white",fg="white",bd=5,relief=GROOVE)
    trackframe.place(x=0,y=0,width=0,height=0)
    
    # Creating Button Frame
    buttonframe = LabelFrame(self.root,text="",bg="white",fg="white",relief=GROOVE)
    buttonframe.place(x=0,y=150,width=50,height=210)
    # Inserting Play Button
    playbtn = Button(buttonframe,text=" ▶",command=self.playsong,width=2,height=1,font=("times new roman",16,"bold"),fg="black",bg="white").grid(row=0,column=0,padx=10,pady=5)
    # Inserting Pause Button
    pausebtn = Button(buttonframe,text="⏸",command=self.pausesong,width=2,height=1,font=("times new roman",16,"bold"),fg="black",bg="white").grid(row=2,column=0,padx=10,pady=5)
    # Inserting Unpause Button
    unpausebtn = Button(buttonframe,text="⏯",command=self.unpausesong,width=2,height=1,font=("times new roman",16,"bold"),fg="black",bg="white").grid(row=3,column=0,padx=10,pady=5)
    # Inserting Stop Button
    stopbtn = Button(buttonframe,text="⏹",command=self.stopsong,width=2,height=1,font=("times new roman",16,"bold"),fg="black",bg="white").grid(row=4,column=0,padx=10,pady=5)

    # Creating Playlist Frame
    songsframe = LabelFrame(self.root,relief=GROOVE)
    songsframe.place(x=600,y=0,width=0,height=0)
    # Inserting Playlist listbox
    self.playlist = Listbox(songsframe, relief=GROOVE)
    # Changing Directory for fetching Songs
    os.chdir("C:/Users/rodri/Documents/Github/FileOrg/fileorg/tema")
    # Fetching Songs
    songtracks = os.listdir()
    # Inserting Songs into Playlist
    for track in songtracks:
      self.playlist.insert(END,track)

  # Defining Play Song Function
  def playsong(self):
    # Displaying Selected Song title
    self.track.set("C:/Users\rodri/Documents/Github/FileOrg/fileorg/tema/tema.mp3")
    # Displaying Status
    self.status.set("-Playing")
    # Loading Selected Song
    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    # Playing Selected Song
    pygame.mixer.music.play()

  def stopsong(self):
    # Displaying Status
    self.status.set("-Stopped")
    # Stopped Song
    pygame.mixer.music.stop()

  def pausesong(self):
    # Displaying Status
    self.status.set("-Paused")
    # Paused Song
    pygame.mixer.music.pause()

  def unpausesong(self):
    # Displaying Status
    self.status.set("-Playing")
    # Playing back Song
    pygame.mixer.music.unpause()

# Passing Root to MusicPlayer Class
MusicPlayer(root)



root.mainloop()