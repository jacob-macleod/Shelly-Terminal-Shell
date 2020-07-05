import subprocess as sp

def core () :
    return "\033[31m" + sp.getoutput("whoami") + "~" + "\033[34m" +  sp.getoutput("pwd") + "/~$ " + "\033[0m"
    sys.stdout.write(u"\u001b[1000D") # Move all the way left again
    sys.stdout.write(u"\u001b[1000D") # Move all the way left again
    sys.stdout.write(u"\u001b[1000D") # Move all the way left again
    sys.stdout.write(u"\u001b[1000D") # Move all the way left again