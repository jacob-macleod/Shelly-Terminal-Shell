line_arr = [[]]
iterator = 0

def split(word): 
    return [char for char in word] 

def user (string) :
    prediction = ""
    with open("command_history.txt", "r") as f:
        #print (line)
        for line in f:
            line_arr[iterator].append(split(line))
            #print (line)
            #print (line_arr)

            for i in range (0, len(string)):
                prediction += line_arr[i][0]
            if prediction == string:
                #print ("Match found")
                return "match found"
            else :
                print ()
                #return "match not found"
        print (line_arr)