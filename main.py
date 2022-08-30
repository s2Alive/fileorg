#imports
from logging import root
from tkinter import *
from tkinter import filedialog
import pygame
import os
import getpass
import os
from datetime import datetime
from requests import delete
import shutil

global pathfile
pathfile = os.getcwd()
pathfile = pathfile.replace("\\", "/")

global musica 
musica = pathfile

# CRIANDO A JANELA 
root = Tk()
root.title('Organizador de pastas')
root.geometry('693x560')
root.config(bg='black')
root.resizable(False, False)

# ADICIONANDO A IMAGEM DE BACKGROUND
img = PhotoImage(file="capa.png")
label = Label(root,image=img)
label.place(x=0, y=0)

#FUNÇÃO PARA PEGAR O DIRETORIO

def directory():
    # ESCOLHE O DIRETORIO 

    filepath=filedialog.askdirectory(title="Selecione a pasta")
    pathfile = filepath
    global fimfim
    fimfim = pathfile
    print (pathfile)
    return pathfile

#ATUALIZAÇÃO DE LISTA



def isChecked():
    Lista_arquivos = ["PowerPoint-{}".format(check1.get()), "Excel-{}".format(check2.get()), "Texto-{}".format(check3.get()), "Word-{}".format(check4.get()), "PDF-{}".format(check5.get()), "Imagens-{}".format(check6.get())]
    try:
        os.chdir(pathfile)
        gol = open("saida.txt","w") 
        L = ["{}".format(Lista_arquivos)]  
        gol.write("") 
        gol.writelines(L)
        gol.close()
    except FileExistsError(delete):
        pass
    return print(Lista_arquivos)

# CHAMANDO FUNÇÂO DO SCRIPT PRO BOTÃO FINAL

def org():
    mover()

#checkbutton

check1 = BooleanVar()
check2 = BooleanVar()
check3 = BooleanVar()
check4 = BooleanVar()
check5 = BooleanVar()
check6 = BooleanVar()


#Criando uma lista

Lista_arquivos = ["PowerPoint-True{}".format(check1.get()), "Excel-{}".format(check2.get()), "Texto-{}".format(check3.get()), "Word-{}".format(check4.get()), "PDF-{}".format(check5.get()), "Imagens-{}".format(check6.get())]  


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


checkbutton2 = Checkbutton (root, bg = "white",activebackground = "blue", text="Excel", var=check2, onvalue=True, offvalue=False, command=isChecked)
checkbutton2.place(x=310, y=350)

checkbutton3 = Checkbutton (root, bg = "white",activebackground = "blue", text="Texto", var=check3, onvalue=True, offvalue=False, command=isChecked)
checkbutton3.place(x=230, y=350)

checkbutton4 = Checkbutton (root, bg = "white",activebackground = "blue", text="Word", var=check4, onvalue=True, offvalue=False, command=isChecked)
checkbutton4.place(x=370, y=400)

checkbutton5 = Checkbutton (root, bg = "white",activebackground = "blue", text="PDF", var=check5, onvalue=True, offvalue=False, command=isChecked)
checkbutton5.place(x=310, y=400)

checkbutton6 = Checkbutton (root, bg = "white",activebackground = "blue", text="Imagens", var=check6, onvalue=True, offvalue=False, command=isChecked)
checkbutton6.place(x=230, y=400)

button = Button(root, bg = "white",text='Organizar pasta',relief=RAISED,font=('Arial Bold', 12), command=org)
button.place(x=290, y=480)



#SCRIPTZAO DAQUI PRA BAIXO #################

usuario = getpass.getuser()
data = datetime.now()



try:
    os.makedirs('logs')
except FileExistsError:
    pass

try:
    log = open("log.txt","w") 
    L = ["\nData:{}".format(data), "\nUsuario que executou o script:{}".format(usuario)]  
    log.write("Informações sobre a execução do script \n \n") 
    log.writelines(L)
    log.close()  

except FileExistsError(delete):
    pass


pathpath = pathfile + "/logs/log.txt"
path2 = pathfile + "/log.txt"
print (pathpath)

src_path = path2
dst_path = pathpath
shutil.move(src_path, dst_path)


#criando pasta da data
def folderdate():
  os.chdir(fimfim)
  try:
    os.makedirs("2022.1")
  except FileExistsError:
    pass


# MOVENDO OS ARQUIVOS
def mover():
  os.chdir(f"{pathfile}")
  ref_arquivo = open("saida.txt","r")
  saida = ref_arquivo.readline()
  if "PowerPoint-True" in saida:
    lista_fim = os.listdir(f"{fimfim}")
    for arquivo in lista_fim:
      if ".pptx" in arquivo:        
            # jogar pra pasta de janeiro 
            try:
              folderdate()                 
              os.rename(f"{fimfim}/{arquivo}", f"{fimfim}/2022.1/{arquivo}")
            except FileNotFoundError:
              print("Não existem powerpoint")

  elif "Excel-True" in saida:
    lista_fim = os.listdir(f"{fimfim}")
    for arquivo in lista_fim:
      if ".xlsx" in arquivo:        
            # jogar pra pasta de janeiro 
            try:
              folderdate()                 
              os.rename(f"{fimfim}/{arquivo}", f"{fimfim}/2022.1/{arquivo}")
            except FileNotFoundError:
              print("Não existem excel")

  elif "Texto-True" in saida:
    lista_fim = os.listdir(f"{fimfim}")
    for arquivo in lista_fim:
      if ".txt" in arquivo:        
            # jogar pra pasta de janeiro 
            try:
              folderdate()                 
              os.rename(f"{fimfim}/{arquivo}", f"{fimfim}/2022.1/{arquivo}")
            except FileNotFoundError:
              print("Não existem texto")
  
  if "Word-True" in saida:
    lista_fim = os.listdir(f"{fimfim}")
    for arquivo in lista_fim:
      if ".doc" in arquivo or ".docx" in arquivo:        
            # jogar pra pasta de janeiro 
            try:
              folderdate()                 
              os.rename(f"{fimfim}/{arquivo}", f"{fimfim}/2022.1/{arquivo}")
            except FileNotFoundError:
              print("Não existem word")
  
  if "PDF-True" in saida:
    lista_fim = os.listdir(f"{fimfim}")
    for arquivo in lista_fim:
      if ".pdf" in arquivo:        
            # jogar pra pasta de janeiro 
            try:
              folderdate()                 
              os.rename(f"{fimfim}/{arquivo}", f"{fimfim}/2022.1/{arquivo}")
            except FileNotFoundError:
              print("Não existem PDF")
  
  if "Imagens-True" in saida:
    lista_fim = os.listdir(f"{fimfim}")
    for arquivo in lista_fim:
      if ".png" in arquivo or ".jpg" in arquivo or ".jpeg" in arquivo or ".webp" in arquivo:        
            # jogar pra pasta de janeiro 
            try:
              folderdate()                 
              os.rename(f"{fimfim}/{arquivo}", f"{fimfim}/2022.1/{arquivo}")
            except FileNotFoundError:
              print("Não existem imagens")
  
  else:
    print("{}".format(saida))
  ref_arquivo.close


# PLAYER DE MUSICA DAQUI PRA BAIXO ################################################################

# Defining MusicPlayer Class
class MusicPlayer:

  # Defining Constructor

  def __init__(self,root):
    self.root = root
    # Title of the window
    self.root.title("Organizador de pastas")
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
    os.chdir(f"{musica}/tema")
    # Fetching Songs
    songtracks = os.listdir()
    # Inserting Songs into Playlist
    for track in songtracks:
      self.playlist.insert(END,track)

  # Defining Play Song Function
  def playsong(self):
    # Displaying Selected Song title
    os.chdir(f"{musica}/tema")
    self.track.set(f"{musica}/tema/tema.mp3")
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