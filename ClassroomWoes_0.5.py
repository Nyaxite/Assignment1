'''
Source file name: ClassroomWoes.py
Last Modified Date: 2013/05/20
Last Modified by: Michael Burnie
Program description: This program uses a series of yes or no questions.
    Be in the life of a college student who has, as usual,
    slept in before class. Now he or she has to write a test, and if he or she
    fails, there are dire consequences! Can you help them get to class and write
    the test?
Version: 0.5
@author: Michael Burnie
'''

import random
import time

def displayIntro():
    print("*-*-*CLASSROOM WOES*-*-*")
    print_pause('You wake up at 7:40. You have class at 8.')
    print_pause('If you miss this class you will miss your final test.')
    print_pause('If you miss your final test, you fail your course.')
    print_pause('If you fail your course, your significant other will')
    print_pause('leave you and your parents disown you. You need to get to class!')
    time.sleep(2)

def print_pause(statement):
    print(statement)
    time.sleep(1)    
    
def getChoice(question):
    isValidInput = False
    fullQuestion = "Do you " + question + "? (yes or no)"
    print(fullQuestion)
    while not(isValidInput):
        getInput = raw_input()
        if getInput == 'y' or getInput == 'yes':
            isValidInput = True
            return 'y'
        elif getInput == 'n' or getInput == 'no':
            isValidInput = True
            return 'n'
        else:
            print(fullQuestion)

def introBreakfast():
    
    print_pause('Your significant other made you breakfast.')
    print_pause("It's that crappy oatmeal again, but you're starving.")
    question = "eat it"
    choice = getChoice(question)
    if choice == 'y':
        print_pause("You eat the oatmeal.")
        print_pause("You get up from the table and you feel your head is hot.")
        print_pause("Was something in that oatmeal?")
        print_pause("You may need help getting to class.")
        print_pause("Driving is not an option, but maybe a walk will clear your head.")
        print_pause("Your significant other offers to drive you.")
    else:
        print_pause("You don't eat the oatmeal.")
        print_pause("You tell your significant other that you don't like their oatmeal.")
        print_pause("They get angry at you, so you sprint out the door, starving.")
        print_pause("You feel like running since the school isn't that far, or ")
        print_pause("you can drive the car to class.")
    return choice

def introTravel(choiceBreakfast):
    
    if choiceBreakfast == 'y':
        question = "get your significant other to drive you"
    else:
        question = "take your car"
        
    choice = getChoice(question)
    
    if choiceBreakfast == 'y' and choice == 'y':
        print_pause("You get your significant other to drive you.")
        print_pause("They are happy to drive you, and comfort you.")
        print_pause("You feel better that they are around.")
        print_pause("You get to class, but only a little late.")
        print_pause("Your significant other offers to let the teacher know")
        print_pause("it was their fault for you being late.")
    elif choiceBreakfast == 'y' and choice == 'n':
        print_pause("You decide to walk.")
        print_pause("The loud noises, busy roads and cloudy skies make you feel worse.")
        print_pause("You find the nearest garbage pail and let your stomach loose.")
        print_pause("It smells like a rotting corpse and it takes minutes before")
        print_pause("your stomach is empty.")
        print_pause("You are now very late to class, but you arrived nonetheless.")
    elif choiceBreakfast == 'n' and choice == 'y':
        print_pause("You take your car.")
        print_pause("You can't help but feel guilty for making your significant other")
        print_pause("feel so bad.")
        print_pause("You keep thinking about this, so you decide to apologize over a text.")
        print_pause("While typing the text, you drive straight into an oncoming truck.")
        print_pause("You're phased, but the need to write this test sparks adrenaline")
        print_pause("like you couldn't even imagine.")
        print_pause("You run to class, leaving the wreckage behind.")
        print_pause("You made it just in time.")
    else:
        print_pause("You decide to run.")
        print_pause("All you can think about is that test.")
        print_pause("You finish the test at 100%!")
        print_pause("'Congratulations! The best final test ever!' your teacher exclaims.")
        print_pause("Your back pocket all of a sudden contains a winning lottery ticket!")
        print_pause("Unfortunately, only seconds later you find people standing over you")
        print_pause("trying to wake you up.")
        print_pause("You briefly passed out halfway to the school because of starvation.")
        print_pause("You make it to class way late, but you may be able to get away with")
        print_pause("it if you sneak in.")
    return choice

def introClassroom(choiceBreakfast, choiceTravel):
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
        print_pause("You allow your significant other to lie for you.")
        print_pause("They say they were bluffing and march into your class")
        print_pause("explaning how terrible of a person you are, and storm out.")
        print_pause("Your teacher and classmates stare at you, with their jaws wide open.")
        print_pause("The teacher slowly walks up to you and")
        print_pause("slams the door in your face.")
        print_pause("You die instantly from shame.")
    elif choiceBreakfast == 'y' and choiceTravel == 'y' and choice == 'n':
        print_pause("You don't allow your significant other to lie for you.")
        print_pause("They think you are the best person ever.")
        print_pause("You don't even care about the test anymore.")
        print_pause("You're just happy the way things are.")
        print_pause("You pass the test regardless, and receive a standing ovation.")
        print_pause("People walk into the classroom to join in on your magnificence.")
        print_pause("You live happily ever after, because like all final tests,")
        print_pause("their grade weight is astronomical.")
    elif choiceBreakfast == 'y' and choiceTravel == 'n' and choice == 'y':
        print_pause("You explain that you're sick.")
        print_pause("The teacher looks sympathetic")
        print_pause("for approximately one second.")
        print_pause("He then says")
        print_pause("'RELEASE THE HOUNDS!' in a most menacing voice.")
        print_pause("You are devoured in seconds.")
        print_pause("At least you don't have that crappy taste in your mouth.")
    elif choiceBreakfast == 'y' and choiceTravel == 'n' and choice == 'n':
        print_pause("You don't explain that you're sick.")
        print_pause("After receiving the test, you are shocked by the questions.")
        print_pause("And not in a good way.")
        print_pause("You proceed to blow chunks out of shock and disgusting oatmeal taste.")
        print_pause("Vomit covers your test and all its pages.")
        print_pause("The teacher reiterates, 'only one test per student!'")
        print_pause("You're screwed. End of story.")
        print_pause("Seriously, everyone thinks you're weird now.")
        print_pause("I shouldn't have to explain you failed the test.")
        print_pause("That was pretty obvious.")
        print_pause("It's covered in vomit, for crying out loud.")
        print_pause("Do you hand it in? (yes or no)")
        time.sleep(2)
        print_pause("Just kidding, you don't get to choose.")
        print_pause("Here's something you can choose though...")
    elif choiceBreakfast == 'n' and choiceTravel == 'y' and choice == 'y':
        print_pause("You tend to your wounds by going to the medical office at the school.")
        print_pause("You wrap bandages all of your body.")
        print_pause("You take some unmarked painkillers.")
        print_pause("This helps you feel much better.")
        print_pause("Until you find out the painkillers are cyanide.")
        print_pause("Unfortunately, today is the one day you forgot to take your")
        print_pause("cyanide antidote.")
        print_pause("You die.")
        print_pause("Dead people typically don't do well on written tests.")
    elif choiceBreakfast == 'n' and choiceTravel == 'y' and choice == 'n':
        print_pause("You don't tend to your wounds.")
        print_pause("Blood is pouring out of you from all angles.")
        print_pause("Luckily, your concentration levels were remarkably high.")
        print_pause("Until you died from blood loss.")
        print_pause("Arguably, your health may have been more important than the test.")
    elif choiceBreakfast == 'n' and choiceTravel == 'n' and choice == 'y':
        print_pause("You sneak into class.")
        print_pause("You begin to think of yourself like an assassin.")
        print_pause("You are navigating between desks like a fly.")
        print_pause("Nobody notices you.")
        print_pause("Or so you think.")
        print_pause("You're so light-headed you don't realize how terrible of a job you're doing.")
        print_pause("You knocked over 12 desks before you realized everyone was watching you.")
        print_pause("The teacher calls the Test Police Brigade.")
        print_pause("They shoot you on the spot.")
        print_pause("Everyone else continues writing as if nothing happened.")
    elif choiceBreakfast == 'n' and choiceTravel == 'n' and choice == 'n':
        print_pause("You don't sneak into class.")
        print_pause("You're such a cool person that everyone thinks you're better than Elvis.")
        print_pause("Or, more likely, they think you're an idiot.")
        print_pause("You can't read minds so you don't know.")
        print_pause("The teacher fails you on the spot for being so cool.")
        print_pause("Or, more likely, for showing up really late looking high.")
        print_pause("It doesn't matter, because you had a dream earlier that was much cooler.")
        print_pause("You die from overconfidence.")
    else:
        print_pause("You have an existential crisis for breaking my code somehow.")
        print_pause("Seriously, what did you do to get here?")
        
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
