import subprocess as sp

# Suggested cursor offset in shellyRC.txt = 23
def core ():
    #Include the git branch if possible
    branch = sp.getoutput("git branch")
    if "fatal" in branch:
        branch = ''
    else: 
        branch = " git:(" + branch + ")"

    return "\033[31m" + sp.getoutput("whoami") + "\033[0m~" + "\033[34m" +  sp.getoutput("pwd") + "\033[32m" + branch + "/\033[0m~$ "
