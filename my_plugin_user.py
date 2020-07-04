line_arr = []
count = 0
string_to_return = ""

def split(word): 
    return [char for char in word] 

def user (string) :
    prediction = ""
    with open("command_history.txt", "r") as f:
        #print (line)
        for line in f:
            #print ("Running on line", line)
            prediction = ""
            line_arr = ""
            count = 0
            string_to_return = ""
            line_arr = split(line)
            line_arr.pop()
            for i in range (0, len(line_arr)) :
                #print (i)
                #print (line_arr[i], end = '')
                #For the line bieng read, look through it and count up the first letters
                if count < len(string) :
                    prediction = prediction + line_arr[i]
                    #print ("Prediction ", prediction, "Count ", count)
                    count = count + 1
                else :
                    if i <= len(line_arr) :
                        string_to_return = string_to_return + line_arr[i]
            if prediction == string and string != "" :
                #print ("Found match on line: ", line)
                #print ("Line is", line)
                #string_to_return = ""
                """
                for i in range(0, count) :
                    if i < len(line_arr) :
                        #print ("\n-------------deleted ", line_arr[i])
                        del line_arr[i]
                        #print ("Line arr now is ", line_arr)
                for i in range (0, len(line_arr)) :
                    string_to_return = string_to_return + line_arr[i]
                """
                #print ("line_arr: ", line_arr, "string to return", string_to_return)
                if len(string_to_return) == 0 :
                    return "\u001b[32m" + string + "\u001b[0m"
                else :
                    string_to_return = "\u001b[31m" + string + "\u001b[37m" + string_to_return + "\u001b[0m"
                return string_to_return
                break
    return string
            

user ('ls -a')