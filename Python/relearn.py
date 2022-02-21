"""
Relearn.py -- a basic program to get back into python
Made by: Quinn S. Kelley
Standalone file. 
"""

import os; ##Incase it isneeded

def nameflip(string:str): 
    """
    Flips a string that is sent into it
    string(str) is a string input into the function
    Returns the flipped string
    """
    flip = "";
    for i in range((string.__len__() - 1),0,-1):
        flip += string[i];
    return flip;


print("Hello again world, Im back") #Lets start with this
val = input("Can you please tell me your name again? \n> ") 
print("Welcome Back " + val + "!")
val = nameflip(val)
print("Flipped: " + val)

