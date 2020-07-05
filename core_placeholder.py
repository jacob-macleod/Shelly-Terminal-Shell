import os

def core (current_dir) :
    current_dir_split = current_dir.split("/")
    del current_dir_split[0]
    print (current_dir_split)
    if len(current_dir.split("/")) == 3:
        return os.environ.get('USER') + "$ "
    return current_dir + " "
