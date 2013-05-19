'''
Source file name: ClassroomWoes.py
Last Modified Date: 2013/05/19
Last Modified by: Michael Burnie
Program description: This program uses a series of yes or no questions.
    Be in the life of a college student who has, as usual,
    slept in before class. Now he or she has to write a test, and if he or she
    fails, there are dire consequences! Can you help them get to class and write
    the test?
Version: 0.3
@author: Michael Burnie
'''

import random
import time

def displayIntro():
    print ('You wake up at 7:40. You have class at 8.')
    print ('If you miss this class you will miss your final test.')
    print ('If you miss your final test, you fail your course.')
    print ('If you fail your course, your significant other will')
    print ('leave you and your parents disown you. You need to get')
    print ('to class!')
    
def getChoice(question):
    isValidInput = False
    print ("Do you " + question + "? (yes or no)")
    while not(isValidInput):
        getInput = raw_input()
        if getInput == 'y' or getInput == 'yes':
            isValidInput = True
            return 'y'
        elif getInput == 'n' or getInput == 'no':
            isValidInput = True
            return 'n'
        else:
            print (question)

def introBreakfast():
    
    print ('Your significant other made you breakfast.')
    time.sleep(1)
    print ("It's that crappy oatmeal again, but you're starving.")
    time.sleep(1)
    question = "eat it"
    choice = getChoice(question)
    if choice == 'y':
        print ("You eat the oatmeal.")
    else:
        print ("You don't eat the oatmeal.")
    return choice

def introTravel(choiceBreakfast):
    
    if choiceBreakfast == 'y':
        question = "get your significant other to drive you"
    else:
        question = "take your car"
        
    choice = getChoice(question)
    
    if choiceBreakfast == 'y' and choice == 'y':
        print ("You get your significant other to drive you.")
    elif choiceBreakfast == 'y' and choice == 'n':
        print ("You decide to walk.")
    elif choiceBreakfast == 'n' and choice == 'y':
        print ("You take your car.")
    else:
        print ("You decide to run.")
    return choice

def introClassroom(choiceBreakfast, choiceTravel):
    if choiceBreakfast == 'y' and choiceTravel == 'y':
        question = "allow your significant other to lie for you"
    elif choiceBreakfast == 'y' and choiceTravel == 'n':
        question = "explain that you're sick to your teacher"
    elif choiceBreakfast == 'n' and choiceTravel == 'y':
        question = "tend to your wounds"   
    else:
        question = "sneak into class"
        
    choice = getChoice(question)
    
    if choiceBreakfast == 'y' and choiceTravel == 'y' and choice == 'y':
        print("You allow your significant other to lie for you.")
    elif choiceBreakfast == 'y' and choiceTravel == 'y' and choice == 'n':
        print("You don't allow your significant other to lie for you.")
    elif choiceBreakfast == 'y' and choiceTravel == 'n' and choice == 'y':
        print("You explain that you're sick.")
    elif choiceBreakfast == 'y' and choiceTravel == 'n' and choice == 'n':
        print("You don't explain that you're sick.")
    elif choiceBreakfast == 'n' and choiceTravel == 'y' and choice == 'y':
        print("You tend to your wounds.")
    elif choiceBreakfast == 'n' and choiceTravel == 'y' and choice == 'n':
        print("You don't tend to your wounds.")
    elif choiceBreakfast == 'n' and choiceTravel == 'n' and choice == 'y':
        print("You sneak into class.")
    elif choiceBreakfast == 'n' and choiceTravel == 'n' and choice == 'n':
        print("You don't sneak into class.")
    else:
        print("You have an existential crisis for breaking my code somehow.")
        
def main():
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        choiceBreakfast = introBreakfast()
        choiceTravel = introTravel(choiceBreakfast)
        introClassroom(choiceBreakfast, choiceTravel)
        
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()
        playAgain.lower()

if __name__ == "__main__": main()
