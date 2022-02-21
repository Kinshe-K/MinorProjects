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
    for i in range((string.__len__() - 1),-1,-1):
        flip += string[i];
    return flip;

def bubblesort(BubbleList:list):
    """
    Sorts a list using the bubble sort method
        Means -- Checks if next term is greater than the next term, if so flip it
    Takes a BubbleList(list) to sort itself
    Then returns the list
    """
    sorted = False
    while sorted == False:
        sorted = True
        for i in range(0, (BubbleList.__len__() - 1) ):
            if BubbleList[i] > BubbleList[i+1]:
                temp = BubbleList[i]
                BubbleList[i] = BubbleList[i+1]
                BubbleList[i+1] = temp
                sorted = False 

def recursive(Val:int): 
    """
    A recursive practive function
    takes in an integer(val), and prints it
    then calls it again
    """
    if Val > 100:
        return str(Val)
    else: 
        strval = ""
        strval += str(Val)
        strval += " " + recursive(Val + 1)
        return strval

print("Hello again world, Im back") #Lets start with this
val = input("Can you please tell me your name again? \n> ") 
print("Welcome Back " + val + "!")
val = nameflip(val)
print("Flipped: " + val)

print("Alright! We got the string flipped. Lets get ready to move onto more complicated things!")

print("Sorting Time!")
a_lis = [20, 10, 6, 2, 100, 92, 9, 1, 11, 52, 10, 0, 6]
bubblesort(a_lis)
print(a_lis)

print("Sorting done! Lets get ready for the next challenge")
print("Recursive time!")
print(recursive(0))

print("So much printing (:")
print("But I think this fun is over for now.")
print("Actual First Project: Just a basic data structure -- nodes, queues, and stacks.")