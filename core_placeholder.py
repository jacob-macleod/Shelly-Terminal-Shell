import subprocess as sp

def core () :
    return "\033[31m" + sp.getoutput("whoami") + "~" + "\033[34m" +  sp.getoutput("pwd") + "/~$ " + "\033[0m"