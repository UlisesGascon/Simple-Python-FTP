# -*- coding: utf-8 -*-
from ftplib import FTP
from sys import argv
import config as DATA
import os

# Terminal var. 
script, foldername, filename = argv

# USER DATA
user_ftp = DATA.user_ftp  # User_ID
passwrd_ftp = DATA.passwrd_ftp  # Password
path_ftp = DATA.path_ftp  # web_address 
input_folder = DATA.input_folder  # Local Folder


ftp = FTP() 
ftp.connect(path_ftp, 21, -999)  # Connection to server
ftp.login(user_ftp, passwrd_ftp)  # Login.
print ftp.getwelcome()  # Welcome Message.


ftp.cwd(foldername) #  Open folder
os.chdir(input_folder)

def bring_file(filename):
	ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
	print "File %r is now in %r!" % (filename, input_folder)

bring_file(filename)

ftp.close() #  Close Connection