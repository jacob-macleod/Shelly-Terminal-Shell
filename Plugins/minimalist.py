import subprocess as sp
# Suggested cursor offset in shellyRC.txt = 33

def core ():
    pwd = sp.getoutput("pwd")
    pwd_arr = pwd.split("/")
    # Delete everything but the first letter of folder names
    del pwd_arr[0]
    for i in range (0, len(pwd_arr) - 1):
        try:
            pwd_arr_string = pwd_arr[i]
            pwd_arr_string = pwd_arr_string[0]
            pwd_arr[i] = pwd_arr_string
        except:
            pass

        # Then change pwd_arr into a string, store into pwd
        pwd = ""
        for i in range(0, len(pwd_arr)):
            pwd += "/" + pwd_arr[i]

        #Include the git branch if possible
        branch = sp.getoutput("git branch")
        if "fatal" in branch:
            branch = ''
        else: 
            branch = " git:(" + branch + ")"

    return "\033[37m" + sp.getoutput("whoami") + "@" + sp.getoutput("hostname") + "\033[35m~" + "\033[35m" +  pwd + "\033[0m~\033[36m" + branch[1:] + "\033[33m~\u2B9E \033[0m"
