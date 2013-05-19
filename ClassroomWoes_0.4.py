'''
Source file name: ClassroomWoes.py
Last Modified Date: 2013/05/19
Last Modified by: Michael Burnie
Program description: This program uses a series of yes or no questions.
    Be in the life of a college student who has, as usual,
    slept in before class. Now he or she has to write a test, and if he or she
    fails, there are dire consequences! Can you help them get to class and write
    the test?
Version: 0.4
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
    fullQuestion = "Do you " + question + "? (yes or no)"
    print (fullQuestion)
    while not(isValidInput):
        getInput = raw_input()
        if getInput == 'y' or getInput == 'yes':
            isValidInput = True
            return 'y'
        elif getInput == 'n' or getInput == 'no':
            isValidInput = True
            return 'n'
        else:
            print (fullQuestion)

def introBreakfast():
    
    print ('Your significant other made you breakfast.')
    time.sleep(1)
    print ("It's that crappy oatmeal again, but you're starving.")
    time.sleep(1)
    question = "eat it"
    choice = getChoice(question)
    if choice == 'y':
        print ("You eat the oatmeal.")
        print ("You get up from the table and you feel your head is hot.")
        print ("Was something in that oatmeal?")
        print ("You may need help getting to class.")
        print ("Driving is not an option, but maybe a walk will clear your head.")
        print ("Your significant other offers to drive you.")
    else:
        print ("You don't eat the oatmeal.")
        print ("You tell your significant other that you don't like their oatmeal.")
        print ("They get angry at you, so you sprint out the door, starving.")
        print ("You feel like running since the school isn't that far, or ")
        print ("you can drive the car to class.")
    return choice

def introTravel(choiceBreakfast):
    
    if choiceBreakfast == 'y':
        question = "get your significant other to drive you"
    else:
        question = "take your car"
        
    choice = getChoice(question)
    
    if choiceBreakfast == 'y' and choice == 'y':
        print ("You get your significant other to drive you.")
        print ("They are happy to drive you, and comfort you.")
        print ("You feel better that they are around.")
        print ("You get to class, only a little late.")
        print ("Your significant other offers to let the teacher know")
        print ("it was their fault for you being late.")
    elif choiceBreakfast == 'y' and choice == 'n':
        print ("You decide to walk.")
        print ("The loud noises, busy roads and cloudy skies make you feel worse.")
        print ("You find the nearest garbage pail and let your stomach loose.")
        print ("It smells like a rotting corpse and it takes minutes before")
        print ("your stomach is empty.")
        print ("You are now very late to class, but you arrived nonetheless.")
    elif choiceBreakfast == 'n' and choice == 'y':
        print ("You take your car.")
        print ("You can't help but feel guilty for making your significant other")
        print ("feel so bad.")
        print ("You keep thinking about this, so you decide to apologize over a text.")
        print ("While typing the text, you drive straight into an oncoming truck.")
        print ("You're phased, but the need to write this test sparks adrenaline")
        print ("like you couldn't even imagine.")
        print ("You run to class, leaving the wreckage behind.")
        print ("You made it just in time.")
    else:
        print ("You decide to run.")
        print ("All you can think about is that test.")
        print ("You finish the test at 100%!")
        print ("'Congratulations! The best final test ever!' your teacher exclaims.")
        print ("Your back pocket all of a sudden contains a winning lottery ticket!")
        print ("Unfortunately, only seconds later you find people standing over you")
        print ("trying to wake you up.")
        print ("You briefly passed out halfway to the school because of starvation.")
        print ("You make it to class way late, but you may be able to get away with")
        print ("it if you sneak in.")
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
        print("You allow your significant other to lie for you.")
        print("They say they were bluffing and march into your class")
        print("explaning how terrible of a person you are, and storm out.")
        print("Your teacher and classmates stare at you, with their jaws wide open.")
        print("The teacher slowly walks up to you and")
        print("slams the door in your face.")
        print("You die instantly from shame.")
    elif choiceBreakfast == 'y' and choiceTravel == 'y' and choice == 'n':
        print("You don't allow your significant other to lie for you.")
        print("They think you are the best person ever.")
        print("You don't even care about the test anymore.")
        print("You're just happy the way things are.")
        print("You pass the test regardless, and receive a standing ovation.")
        print("People walk into the classroom to join in on your magnificence.")
        print("You live happily ever after, because like all final tests,")
        print("their grade weight is astronomical.")
    elif choiceBreakfast == 'y' and choiceTravel == 'n' and choice == 'y':
        print("You explain that you're sick.")
        print("The teacher looks sympathetic")
        print("for approximately one second.")
        print("He then says")
        print("'RELEASE THE HOUNDS!' in a most menacing voice.")
        print("You are devoured in seconds.")
        print("At least you don't have that crappy taste in your mouth.")
    elif choiceBreakfast == 'y' and choiceTravel == 'n' and choice == 'n':
        print("You don't explain that you're sick.")
        print("After receiving the test, you are shocked by the questions.")
        print("And not in a good way.")
        print("You proceed to blow chunks out of shock and disgusting oatmeal taste.")
        print("Vomit covers your test and all its pages.")
        print("The teacher reiterates, 'only one test per student!'")
        print("You're screwed. End of story.")
        print("Seriously, everyone thinks you're weird now.")
        print("I shouldn't have to explain you failed the test.")
        print("That was pretty obvious.")
        print("It's covered in vomit, for crying out loud.")
        print("Do you hand it in? (yes or no)")
        print("Just kidding, you don't get to choose.")
        print("Here's something you can choose though...")
    elif choiceBreakfast == 'n' and choiceTravel == 'y' and choice == 'y':
        print("You tend to your wounds by going to the medical office at the school.")
        print("You wrap bandages all of your body.")
        print("You take some unmarked painkillers.")
        print("This helps you feel much better.")
        print("Until you find out the painkillers are cyanide.")
        print("Unfortunately, today is the one day you forgot to take your")
        print("cyanide antidote.")
        print("You die.")
        print("Dead people typically don't do well on written tests.")
    elif choiceBreakfast == 'n' and choiceTravel == 'y' and choice == 'n':
        print("You don't tend to your wounds.")
        print("Blood is pouring out of you from all angles.")
        print("Luckily, your concentration levels were remarkably high.")
        print("Until you died from blood loss.")
        print("Arguably, your health may have been more important than the test.")
    elif choiceBreakfast == 'n' and choiceTravel == 'n' and choice == 'y':
        print("You sneak into class.")
        print("You begin to think of yourself like an assassin.")
        print("You are navigating between desks like a fly.")
        print("Nobody notices you.")
        print("Or so you think.")
        print("You're so light-headed you don't realize how terrible of a job you're doing.")
        print("You knocked over 12 desks before you realized everyone was watching you.")
        print("The teacher calls the Test Police Brigade.")
        print("They shoot you on the spot.")
        print("Everyone else continues writing as if nothing happened.")
    elif choiceBreakfast == 'n' and choiceTravel == 'n' and choice == 'n':
        print("You don't sneak into class.")
        print("You're such a cool person that everyone thinks you're better than Elvis.")
        print("Or, more likely, they think you're an idiot.")
        print("You can't read minds so you don't know.")
        print("The teacher fails you on the spot for being so cool.")
        print("Or, more likely, for showing up really late looking high.")
        print("It doesn't matter, because you had a dream earlier that was much cooler.")
        print("You die from overconfidence.")
    else:
        print("You have an existential crisis for breaking my code somehow.")
        print("Seriously, what did you do to get here?")
        
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
