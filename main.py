# Import modules
import os, sys, tty, termcolor, termios

#Define 2 variables
global core_plugin_location
global user_plugin_location

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)


#Reads ShellyRC.txt to find file location of core and user plugin
def find_plugin_location () :
    #Set 2 variables as global
    global core_plugin_location
    global user_plugin_location

    with open("shellyRC.txt") as rc:
        for line in rc:
            #Look for file locations in each line
            line_arr = line.split('"')
            # Hash denotes the file location of the core plugin, ! denotes the file location of the user plugin
            if '#' in line_arr[0] :
                core_plugin_location = line_arr[1]
            elif '!' in line_arr[0] :
                user_plugin_location = line_arr[1]


find_plugin_location()

#Copyies contents of each plugin file to the appropiate placeholder file
def write_to_placeholder_files (core_file_location, user_file_location) :
    with open(core_file_location) as f:
        with open("core_placeholder.py", "w") as f1:
            for line in f:
                f1.write(line)

    with open(user_file_location) as f:
        with open("user_placeholder.py", "w") as f1:
            for line in f:
                f1.write(line)

write_to_placeholder_files(core_plugin_location, user_plugin_location)

#Once the plugin contents are copied to the placeholder files, the appropiate plugins can be imported
from core_placeholder import core
from user_placeholder import user


index = 0
input = ""


def command_line():
    tty.setraw(sys.stdin)
    while True: # loop for each line
    # Define data-model for an input-string with a cursor
        input = ""
        index = 0
        while True: # loop for each character
            char = ord(sys.stdin.read(1)) # read one char and get char code

            # ELif char == CTR-C
            if char == 3:
                return

            elif 32 <= char <= 126:
                #Store letter in index
                input = input[:index] + chr(char) + input[index:]
                index += 1

            elif char in {10, 13}:
                sys.stdout.write(u"\u001b[1000D")
                print ()
                #Save command to txt file
                with open("command_history.txt", "a+") as f:
                    f.write(input + "\n")

                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                os.system(input)
                tty.setraw(sys.stdin)
                input = ""
                index = 0

            elif char == 27:
                next1, next2 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
                if next1 == 91:
                    if next2 == 68: # Left
                        index = max(0, index - 1)
                    elif next2 == 67: # Right
                        index = min(len(input), index + 1)

            #Elif char == backspace
            elif char == 127 :
                input = input[:index-1] + input[index:]
                index -= 1

            # Print current input-string
            sys.stdout.write(u"\u001b[1000D") # Move all the way left
            sys.stdout.write(u"\u001b[2K")    # Clear the line
            output = core() + user(input)
            sys.stdout.write(output)
            #sys.stdout.write("\u001b[31m" + input + "\u001b[37m" + "string_to_return" + "")
            sys.stdout.write(u"\u001b[1000C") # Move all the way left again

            if index > 0:
                sys.stdout.write(u"\u001b[" + str(index) + "C") # Move cursor too index
            sys.stdout.flush()

command_line()