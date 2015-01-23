# -*- coding: utf-8 -*-
from ftplib import FTP
import config as DATA

# USER DATA
user_ftp = DATA.user_ftp  # User_ID
passwrd_ftp = DATA.passwrd_ftp  # Password
path_ftp = DATA.path_ftp  # web_address 


ftp = FTP() 
ftp.connect(path_ftp, 21, -999)  # Connection to server
ftp.login(user_ftp, passwrd_ftp)  # Login.
print ftp.getwelcome()  # Welcome Message.

#  Crear un nuevo directorio

data = []

ftp.dir(data.append)

ftp.quit()

for line in data:
    print "-", line


ftp.close() #  Close Connection