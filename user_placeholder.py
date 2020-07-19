import os

#Initialise various variables
line_arr = []
count = 0
string_to_return = ""

#Function to split a string into an array
def split(word): 
    return [char for char in word] 

def user (string, command_history_file, coloured):
    prediction = ""
    with open(command_history_file, "r") as f:
        for line in f:
            #print ("Running on line", line)
            prediction = ""
            line_arr = ""
            count = 0
            string_to_return = ""
            line_arr = split(line)
            #Remove last item of line_arr
            line_arr.pop()
            
            #If x characters in user's text(so far) save first x characters in line_arr to variable prediction
            for i in range (0, len(line_arr)):
                #For the line being read, look through it and count up the first letters
                if count < len(string):
                    prediction = prediction + line_arr[i]
                    count = count + 1
                else :
                    if i <= len(line_arr):
                        string_to_return = string_to_return + line_arr[i]

            #If prediction is the same as the user's text, return the users text + (the predicted text - the user's text)(simplified)
            if prediction == string and string != "":
                if len(string_to_return) == 0:
                    return "\u001b[32m" + string + "\u001b[0m"
                else :
                    if coloured == True :
                        string_to_return = "\u001b[31m" + string + "\u001b[37m" + string_to_return + "\u001b[0m"
                    else :
                        string_to_return = string + string_to_return
                return string_to_return
                break
    #If no match is found, just return the user's text noramally
    return string