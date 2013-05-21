'''
Source file name: ClassroomWoes.py
Last Modified Date: 2013/05/20
Last Modified by: Michael Burnie
Program description: This program uses a series of yes or no questions.
    Be in the life of a college student who has, as usual,
    slept in before class. Now he or she has to write a test, and if he or she
    fails, there are dire consequences! Can you get to class and write
    the test? Or will you explore the hilarious ways to die?
    There are currently three decision levels: Breakfast, Travel and Classroom.
Version: 1.0
@author: Michael Burnie
'''

import time

'''
displayIntro introduces the player to the story, describing the awful things that
will happen to this poor student if they don't get to class in a series of print statements.
'''
def displayIntro():
    print("*-*-*CLASSROOM WOES*-*-*")
    printPause('You wake up at 7:40. You have class at 8.')
    printPause('If you miss this class you will miss your final test.')
    printPause('If you miss your final test, you fail your course.')
    printPause('If you fail your course, your significant other will')
    printPause('leave you and your parents disown you. You need to get to class!')
    time.sleep(2)

'''
printPause() uses the print() function with a time.sleep(1) to add a short pause
after each break, instead of displaying the entire block of text all at once.
This function saves the need to do a time.sleep(num) manually after every print().
An asterisk is displayed before each statement, signalling no user input is required.
'''
def printPause(statement):
    print("* " + statement)
    time.sleep(1)    

'''
getChoice() displays and validates user input. It takes a String parameter called question. 
Every time question needs to be asked, a part of the question is sent to this method,
and this method creates a complete phrase with it. getChoice() also converts user input
to lower. The question will repeat along with an error message if the user types 
incorrect input. >> and << are displayed around the question to signal user input.
'''
def getChoice(question):
    isValidInput = False
    fullQuestion = ">> Do you " + question + "? (yes or no) <<"
    print(fullQuestion) #display the entire question
    while not(isValidInput):
        getInput = raw_input() #get the input from the user. This input is used multiple times in the code
        getInput = getInput.lower() #convert the string to a lower, to allow for more combinations of choices
        if getInput == 'y' or getInput == 'yes': #the user entered 'yes' as the choice
            isValidInput = True #input is valid
            return 'y' #return yes
        elif getInput == 'n' or getInput == 'no': #the user entered 'no' as the choice
            isValidInput = True #input is valid
            return 'n' #return no
        else:
            #input is invalid, rerun loop
            print("Invalid input! Please enter 'y', 'yes', 'n' or 'no' to answer a question.")
            print(fullQuestion) #display the entire question

'''
displayBreakfast() is the first decision structure. It simply has a choice 
for whether the player wishes to have breakfast or not. To proceed in the right direction,
the player must choose to have breakfast.
'''
def displayBreakfast():
    
    printPause('Your significant other made you breakfast.')
    printPause("It's that crappy oatmeal again, but you're starving.")
    question = "eat it" #question fragment sent to getChoice()
    choice = getChoice(question) #call getChoice() with the question fragment
    if choice == 'y': #correct choice
        printPause("You eat the oatmeal.")
        printPause("You get up from the table and you feel your head is hot.")
        printPause("Was something in that oatmeal?")
        printPause("You may need help getting to class.")
        printPause("Driving is not an option, but maybe a walk will clear your head.")
        printPause("Your significant other offers to drive you.")
    else:
        printPause("You don't eat the oatmeal.")
        printPause("You tell your significant other that you don't like their oatmeal.")
        printPause("They get angry at you, so you sprint out the door, starving.")
        printPause("You feel like running since the school isn't that far, or ")
        printPause("you can drive the car to class.")
    return choice

'''
displayTravel() is the second decision structure. Depending on the choice made
in displayBreakfast(), they will receive different outcomes here, and different
decisions to make. To proceed in the right direction, the player must
have chosen to have breakfast and to let their S/O to drive them.
'''
def displayTravel(choiceBreakfast):
    
    if choiceBreakfast == 'y':
        question = "get your significant other to drive you"
    else:
        question = "take your car"
        
    choice = getChoice(question)
    
    if choiceBreakfast == 'y' and choice == 'y': #correct choice
        printPause("You get your significant other to drive you.")
        printPause("They are happy to drive you, and comfort you.")
        printPause("You feel better that they are around.")
        printPause("You get to class, but only a little late.")
        printPause("Your significant other offers to let the teacher know")
        printPause("it was their fault for you being late.")
    elif choiceBreakfast == 'y' and choice == 'n':
        printPause("You decide to walk.")
        printPause("The loud noises, busy roads and cloudy skies make you feel worse.")
        printPause("You find the nearest garbage pail and let your stomach loose.")
        printPause("It smells like a rotting corpse and it takes minutes before")
        printPause("your stomach is empty.")
        printPause("You are now very late to class, but you arrived nonetheless.")
    elif choiceBreakfast == 'n' and choice == 'y':
        printPause("You take your car.")
        printPause("You can't help but feel guilty for making your significant other feel terrible")
        printPause("You keep thinking about this, so you decide to apologize over a text.")
        printPause("While typing the text, you drive straight into an oncoming truck.")
        printPause("You're phased, but the need to write this test sparks adrenaline")
        printPause("like you couldn't even imagine.")
        printPause("You run to class, leaving the wreckage behind.")
        printPause("You made it just in time.")
    else:
        printPause("You decide to run.")
        printPause("All you can think about is that test.")
        printPause("You finish the test at 100%!")
        printPause("'Congratulations! The best final test ever!' your teacher exclaims.")
        printPause("Your back pocket all of a sudden contains a winning lottery ticket!")
        printPause("Unfortunately, only seconds later you find people standing over you")
        printPause("trying to wake you up.")
        printPause("You briefly passed out halfway to the school because of starvation.")
        printPause("You make it to class way late, but you may be able to get away with")
        printPause("it if you sneak in.")
    return choice

'''
displayClassroom() is the third decision structure. Depending on the choice made
in displayBreakfast() and displayTravel, they will receive different outcomes here, 
and different decisions to make. To proceed in the right direction, the player must
have chosen to have breakfast, to let their S/O to drive them and to NOT allow their
S/O to lie for them. Otherwise, the player loses the game in one of 7 different and funny ways.
'''
def displayClassroom(choiceBreakfast, choiceTravel):
    if choiceBreakfast == 'y' and choiceTravel == 'y':
        question = "allow your significant other to lie for you"
    elif choiceBreakfast == 'y' and choiceTravel == 'n':
        question = "explain that you're sick to your teacher"
    elif choiceBreakfast == 'n' and choiceTravel == 'y':
        question = "tend to your wounds before the test"   
    else:
        question = "sneak into class"
        
    choice = getChoice(question)
    
    if choiceBreakfast == 'y' and choiceTravel == 'y' and choice == 'y':
        printPause("You allow your significant other to lie for you.")
        printPause("They say they were bluffing and march into your class")
        printPause("explaning how terrible of a person you are, and storm out.")
        printPause("Your teacher and classmates stare at you, with their jaws wide open.")
        printPause("The teacher slowly walks up to you and")
        printPause("slams the door in your face.")
        printPause("You die instantly from shame.")
    elif choiceBreakfast == 'y' and choiceTravel == 'y' and choice == 'n': #correct choice
        printPause("You don't allow your significant other to lie for you.")
        printPause("They think you are the best person ever.")
        printPause("You don't even care about the test anymore.")
        printPause("You're just happy the way things are.")
        printPause("You pass the test regardless, and receive a standing ovation.")
        printPause("People walk into the classroom to join in on your magnificence.")
        printPause("You live happily ever after, because like all final tests,")
        printPause("their grade weight is astronomical.")
    elif choiceBreakfast == 'y' and choiceTravel == 'n' and choice == 'y':
        printPause("You explain that you're sick.")
        printPause("The teacher looks sympathetic")
        printPause("for approximately one second.")
        printPause("He then says")
        printPause("'RELEASE THE HOUNDS!' in a most menacing voice.")
        printPause("You are devoured in seconds.")
        printPause("At least you don't have that crappy taste in your mouth.")
    elif choiceBreakfast == 'y' and choiceTravel == 'n' and choice == 'n':
        printPause("You don't explain that you're sick.")
        printPause("After receiving the test, you are shocked by the questions.")
        printPause("And not in a good way.")
        printPause("You proceed to blow chunks out of shock and disgusting oatmeal taste.")
        printPause("Vomit covers your test and all its pages.")
        printPause("The teacher reiterates, 'only one test per student!'")
        printPause("You're screwed. End of story.")
        printPause("Seriously, everyone thinks you're weird now.")
        printPause("I shouldn't have to explain you failed the test.")
        printPause("That was pretty obvious.")
        printPause("It's covered in vomit, for crying out loud.")
        printPause("Do you hand it in? (yes or no)")
        time.sleep(2)
        printPause("Just kidding, you don't get to choose.")
        printPause("Here's something you can choose though...")
    elif choiceBreakfast == 'n' and choiceTravel == 'y' and choice == 'y':
        printPause("You tend to your wounds by going to the medical office at the school.")
        printPause("You wrap bandages all of your body.")
        printPause("You take some unmarked painkillers.")
        printPause("This helps you feel much better.")
        printPause("Until you find out the painkillers are cyanide.")
        printPause("Unfortunately, today is the one day you forgot to take your")
        printPause("cyanide antidote.")
        printPause("You die.")
        printPause("Dead people typically don't do well on written tests.")
    elif choiceBreakfast == 'n' and choiceTravel == 'y' and choice == 'n':
        printPause("You don't tend to your wounds.")
        printPause("Blood is pouring out of you from all angles.")
        printPause("Luckily, your concentration levels were remarkably high.")
        printPause("Until you died from blood loss.")
        printPause("Arguably, your health may have been more important than the test.")
    elif choiceBreakfast == 'n' and choiceTravel == 'n' and choice == 'y':
        printPause("You sneak into class.")
        printPause("You begin to think of yourself like an assassin.")
        printPause("You are navigating between desks like a fly.")
        printPause("Nobody notices you.")
        printPause("Or so you think.")
        printPause("You're so light-headed you don't realize how terrible of a job you're doing.")
        printPause("You knocked over 12 desks before you realized everyone was watching you.")
        printPause("The teacher calls the Test Police Brigade.")
        printPause("They shoot you on the spot.")
        printPause("Everyone else continues writing as if nothing happened.")
    elif choiceBreakfast == 'n' and choiceTravel == 'n' and choice == 'n':
        printPause("You don't sneak into class.")
        printPause("You're such a cool person that everyone thinks you're better than Elvis.")
        printPause("Or, more likely, they think you're an idiot.")
        printPause("You can't read minds so you don't know.")
        printPause("The teacher fails you on the spot for being so cool.")
        printPause("Or, more likely, for showing up really late looking high.")
        printPause("It doesn't matter, because you had a dream earlier that was much cooler.")
        printPause("You die from overconfidence.")
    else:
        printPause("You have an existential crisis for breaking my code somehow.")
        printPause("Seriously, what did you do to get here?")

'''
The main() class calls the intro methods and the three decision methods.
It also handles whether the user wishes to play again, calling the getChoice() method.
''' 
def main():
    playAgain = 'y'
    while playAgain == 'y':
        displayIntro() #display the intro text
        choiceBreakfast = displayBreakfast() #display the breakfast decision tree (1st) and get the player's choice
        choiceTravel = displayTravel(choiceBreakfast) #display the travel decision tree (2nd) and get the player's choice
        displayClassroom(choiceBreakfast, choiceTravel) #display the classroom decision tree (3rd)
        
        playAgain = getChoice("want to play again")
    print("Thanks for playing!")
    
if __name__ == "__main__": main() #run main
