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
output_folder = DATA.output_folder  # Local Folder


ftp = FTP() 
ftp.connect(path_ftp, 21, -999)  # Connection to server
ftp.login(user_ftp, passwrd_ftp)  # Login.
print ftp.getwelcome()  # Welcome Message.


ftp.cwd(foldername)  #  FTP Server Folder
os.chdir(output_folder)  # Local Folder

def upload_file(filename):
	thefile = open(filename, 'r')
	ftp.storlines('STOR ' + filename, thefile)
	thefile.close()
	print "File %r is now in FTP Server under %r!" % (filename, output_folder)

upload_file(filename)

ftp.close() #  Close Connection