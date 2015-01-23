# -*- coding: utf-8 -*-
from ftplib import FTP
from sys import argv
import config as DATA

# Terminal var. 
script, foldername = argv

# USER DATA
user_ftp = DATA.user_ftp  # User_ID
passwrd_ftp = DATA.passwrd_ftp  # Password
path_ftp = DATA.path_ftp  # web_address 


ftp = FTP() 
ftp.connect(path_ftp, 21, -999)  # Connection to server
ftp.login(user_ftp, passwrd_ftp)  # Login.
print ftp.getwelcome()  # Welcome Message.

#  Crear un nuevo directorio
def make_directory(directory_name='new-dir'):
	'''
	New directory in the server. In case of no name provided. It will create "new-dir"
	'''
	ftp.mkd(directory_name)
	ftp.cwd(directory_name)
	print ftp.pwd()

make_directory(foldername)

ftp.close() #  Close Connection