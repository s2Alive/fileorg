#script que vai organizar as pastas

#imports
from distutils import file_util
from distutils.file_util import move_file
import getpass
import os
from pathlib import Path
from datetime import datetime
from requests import delete
import shutil

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

src_path = r"C:/Users/rodri/Documents/Github/FileOrg/fileorg/log.txt"
dst_path = r"C:/Users/rodri/Documents/Github/FileOrg/fileorg/logs/log.txt"
shutil.move(src_path, dst_path)

