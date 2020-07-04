line_arr = []
count = 0

def split(word): 
    return [char for char in word] 

def user (string) :
    prediction = ""
    with open("command_history.txt", "r") as f:
        #print (line)
        for line in f:
            #print ("Running on line", line)
            prediction = ""
            count = 0
            line_arr = split(line)
            for i in range (0, len(line_arr)) :
                #print (i)
                #print (line_arr[i], end = '')
                #For the line bieng read, look through it and count up the first letters
                if count < len(string) :
                    prediction = prediction + line_arr[i]
                    #print ("Prediction ", prediction, "Count ", count)
                    count = count + 1
            if prediction == string :
                #print ("Found match on line: ", line)
                #print ("Line is", line)
                return line
                break
    return string
            

user ('l')