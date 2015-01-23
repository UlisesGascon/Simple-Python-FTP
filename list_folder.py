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


ftp.cwd(foldername) #  Open folder

def list_folder():
	print "File List: "
	files = ftp.dir()
	print files

list_folder()


ftp.close() #  Close Connection