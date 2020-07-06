#!/usr/bin/env python

#Installs shelly shell
print ("Welcome to the shelly installation! Make sure you install python 3 and git command line interface before installing shelly.")
response = input("1: Install the shell with default plugins\n2: Use default core plugin and choose custom user plugin\n3: Use default user plugin and use custom core plugin\n4: Use custom core and user plugin: ")
if response == 1 :
    os.system("git clone https://github.com/jacob-macleod/Shelly-Terminal-Shell.git")
    os.system("chmod +x Shelly-Terminal-Shell/main.py")