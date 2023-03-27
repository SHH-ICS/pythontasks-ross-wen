# TASK: Update both functions to reverse the letters in the name and provide the square root of the users age.
import math

def reverseName(myName):
    myNameReversed = []
    for x in myName:
        myNameReversed.insert(0,x)
    myName = (''.join(myNameReversed))
    result = myName
    return result
  
def rootAge(myAge):
    myAge = math.sqrt(myAge)
    result = myAge
    return result
  
me = input("What is your name? ")
im = float(input("What is your age? "))

print("Your name in reverse is: ",reverseName(me))
print("The square root of your age is: ",rootAge(im))
