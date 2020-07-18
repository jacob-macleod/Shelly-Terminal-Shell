# Import modules
import os
import sys
import tty
import termios
import subprocess   

command_history_location = os.getcwd() + "/" + "command_history.txt"

# Define variables
global core_plugin_location
global user_plugin_location
global arrow_count
global alias_names
global alias_commands

#Assign values 
alias_names = []
alias_commands = []

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)


# Splits string by word
def split(string):
    word = ""
    string_arr = []
    for char in string:
        if char == ' ':
           string_arr.append(word)
           string_arr.append(char)
           word = ""
        else:
            word += char
    string_arr.append(word)
    return (string_arr)



# Reads ShellyRC.txt to find file location of core and user plugin
def find_plugin_location():
    # Set 2 variables as global
    global core_plugin_location
    global user_plugin_location
    global alias_names
    global alias_commands


    with open("shellyRC.txt") as rc:
        for line in rc:
            # Look for file locations in each line
            line_arr = line.split('"')
            # Hash denotes the file location of the core plugin
            #  ! denotes the file location of the user plugin
            # % Denotes the alias name and command
            if '#' in line_arr[0]:
                core_plugin_location = line_arr[1]
            elif '!' in line_arr[0]:
                user_plugin_location = line_arr[1]
            elif '%' in line_arr[0]:
                alias_names.append(line_arr[1])
                alias_commands.append(line_arr[3])



find_plugin_location()


# Copyies contents of each plugin file to the appropiate placeholder file
def write_to_placeholder_files(core_file_location, user_file_location):
    with open(core_file_location) as f:
        with open("core_placeholder.py", "w") as f1:
            for line in f:
                f1.write(line)

    with open(user_file_location) as f:
        with open("user_placeholder.py", "w") as f1:
            for line in f:
                f1.write(line)


write_to_placeholder_files(core_plugin_location, user_plugin_location)


# Once the plugin contents are copied to the placeholder files,
#  the appropiate plugins can be imported
from core_placeholder import core
from user_placeholder import user


index = 0
input = ""


def command_line():
    #Define up arrow count as a global varible then set a value to it
    global arrow_count
    arrow_count = 0
    
    match_found = False


    tty.setraw(sys.stdin)
    while True:
        # Define data-model for an input-string with a cursor
        input = ""
        index = 0
        while True:  # loop for each character
            char = ord(sys.stdin.read(1))  # read one char and get char code

            # ELif char == CTR-C
            if char == 3:
                return

            elif 32 <= char <= 126:
                # Store letter in index
                input = input[:index] + chr(char) + input[index:]
                index += 1

            elif char in {10, 13}:
                sys.stdout.write(u"\u001b[1000D")
                print()
                # Save command to txt file
                with open(command_history_location, "a+") as f:
                    f.write("\n" + input)
                
                arrow_count = 0

                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                if input != "" and input != " " and input != "  " and input != "   ":
                    if input.split()[0] == "ls":
                        input += " --color"

                    for i in range (0, len(alias_names)):
                        # If word user types can be substituted for an alias_phrase
                        if alias_names[i] in input :
                            # Calls split function to split input by word
                            input_arr = split(input)
                            match_found = True

                            # Cycles through input_arr and looks for a phrase to subsititute with an alias command - .deb turns into sudo dpkg
                            for _ in range (0, len(input_arr)):
                                if input_arr[_] == alias_names[i]:
                                    # Substitute alias name with alias command
                                    input_arr[_] = alias_commands[i]

                                    # Turn input_arr into a string
                                    input = ""
                                    for element in range(0, len(input_arr)):
                                        input += input_arr[element]

                                    # Check if the command is ls - if so, color it
                                    if input.split()[0] == "ls":
                                        input += " --color"

                                    # Execute the whole command
                                    os.system(input)

                    if match_found == False :
                        os.system(input)

                    match_found = False

                    # Changing directories:
                    try:
                        os.chdir(input.split(" ")[1])
                    except:
                        pass

                    # The 'exit' command:
                    if input == "exit" or input == "exit " or input == " exit":
                        sys.exit()

                tty.setraw(sys.stdin)
                input = ""
                index = 0

            elif char == 27:
                next1, next2 = ord(sys.stdin.read(1)), ord(sys.stdin.read(1))
                if next1 == 91:
                    if next2 == 68:  # Left
                        index = max(0, index - 1)
                    elif next2 == 67:  # Right
                        index = min(len(input), index + 1)
                    #Elif up arrow is pressed
                    elif next2 == 65:
                        with open('command_history.txt', 'r') as f:
                            lines = f.read().splitlines()
                            arrow_count += 1
                            if arrow_count < len(lines) + 1 :
                                input = lines[-arrow_count]
                            else :
                                arrow_count -=1
                    #Elif down arrow is being pressed
                    elif next2 == 66:
                        with open('command_history.txt', 'r') as f:
                            arrow_count -= 1
                            lines = f.read().splitlines()
                            if arrow_count > 0 :
                                input = lines[- arrow_count]
                            else :
                                arrow_count += 1


            # Elif char == backspace
            elif char == 127:
                input = input[:index-1] + input[index:]
                index -= 1


            # Print current input-string
            sys.stdout.write(u"\u001b[1000D")  # Move all the way left
            sys.stdout.write(u"\u001b[2K")    # Clear the line
            output = core() + user(input, command_history_location)
            sys.stdout.write(output)
            # sys.stdout.write("\u001b[31m" + input + "\u001b[37m" + "string_to_return" + "")
            sys.stdout.write(u"\u001b[1000C")  # Move all the way left again

            if index > 0:
                sys.stdout.write(u"\u001b[" + str(index) + "C") 
            # Move cursor too index
            sys.stdout.flush()

command_line()
