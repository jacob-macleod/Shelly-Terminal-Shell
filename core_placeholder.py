import os

def split(word): 
    return [char for char in word] 

def core (current_dir) :
    str_username = ""
    username = split(os.popen("whoami").read())
    username.pop()

    for i in range (0, len(username)) :
        str_username += username[i]
    current_dir_split = current_dir.split()
    del current_dir_split[0]
    if len(current_dir.split("/")) == 3:
        
        return str_username + "$ "
    return str_username + "@" + current_dir + "$ "

#Todo: remove first slash of the current directory, add syntax highlihhting, git support