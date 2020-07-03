def user (string) :
    with open("command_history.txt", "w") as f1:
        for line in f:
            #DO autocompletion on each line
            if string == 'l':
                return string + "\u001b[31ms\u001b[0m"
            else :
                return string