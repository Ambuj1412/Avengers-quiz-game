#Quiz Questions:
string_easy = """*Billionaire, CEO, genius, and builder of robot suits. Everyone needs a hobby. -- __1__.
*Amazing combat powers, great fighting suit, enhanced strength thanks to a very
 particular herb, and  Oh, Yes!!!  a king, too. -- __2__.
*Spy, assassin and double agent, this combat veteran has gone underground following
 recent disagreements with her former allies. -- __3__.
*He floats, he is got a gem in his head, and he is a robot. -- __4__."""

string_medium = """*He is the guy how took GO GREEN Too seriously. -- __1__.
*The Sorcerer Supreme of Earth and a former surgeon, you know, no big deal. -- __2__.
*Assassin, bounty hunter, and last of her kind, with some serious trouble headed her way from her
 adoptive father. -- __3__.
*This hero has lost his home, his weapon of choice, and even one of his eyes but
 at least he has a great haircut. -- __4__. """

string_difficult = """*He really hopes you have heard of him. His ethics can be a bit questionable sometimes,
 but his heart is (usually) in the right place. -- __1__.
*A bio-engineered animal with a tongue nearly as deadly as his (many, many) guns. -- __2__.
*After battling the Avengers in a bid for revenge on Tony- Stark, this powerful psychic
 was persuaded to swap sides and join forces. -- __3__.
*Despotic titan who thinks the universe has an overpopulation problem.
 Also has a big glove in need of decoration. -- __4__. """

string_bonus = """*I am __1__.
*I can do this all __2__.
*I am/we are __3__.
*I am with you till the __4__ of the __5__.
*That is my __6__ captain america. I am always __7__. """

#Quiz answers:
answers_easy = ["iron man","black panther","black widow","vision"]

answers_medium = ["hulk", "doctor strange", "gamora", "thor"]

answers_difficult = ["star lord","rocket","scarlet witch","thanos"]

answers_bonus = ["iron man", "day","groot","end","line","secret","angry"]



def choices():
    #this function will choose difficulity level of the game -- easy, medium or difficult.
    user_level = input("\nSelect the mode of Difficulty -- easy, medium, difficult: ").lower()
    #.lower() is used to make game less case senstive,
    #i.e, in user user inputs a catial laetter
    if user_level == "easy":
        print ("\nYou have selected Easy Level.")
        quiz(string_easy,answers_easy)
    elif user_level == "medium":
        print ("\nYou have selected Medium Level.")
        quiz(string_medium,answers_medium)
    elif user_level == "difficult":
        print("\nYou have selected difficult Level.")
        quiz(string_difficult,answers_difficult)
    else:
        print("\nError!!!. Please try again.")
        choice = choices()#in case user input other than the given choices.



import sys#sys is imported to terminate the program.
def play_again():
    #this function for playing game in case you lose and want to play again after winning
    retry = input("\nDo you want play again (yes/no): ").lower()
    if retry == "yes":
        gameplay()#this will bring the user back to beginning of the game.
    elif retry == "no":
        sys.exit()#this will terminate the program and user will exit the game
    else:
        print("\nError!!!. Please try again.")
        play_again()#in case user input other than the given choices.



def bonus_play():
    #bonus_play is created in case if user clear the selected mode of game that unlocks the bonus ground
    #and choose whether to play it or not
    print("\nCongratulations! You Won!")
    print("\nYou have Unlocked the BONUS level!!!!!")
    bonus_input = input("\nDo you want to play BONUS level (yes/no): ").lower()
    #.lower() is used to make game less case senstive,
    #i.e, in user user inputs a catial laetter
    if bonus_input == "yes":
        print("\nYou have fill-the-blanks in these famous Avengers dialogues.")
        print("\nYou will get ONLY 2 GUESSES per blank.")
        guesses = 2
        bonus_quiz(string_bonus,answers_bonus,guesses)
    elif bonus_input == "no":
        sys.exit()#this will terminate the program and user will exit the game
    else:
        print("\nError!!!. Please try again.")
        bonus_play()#in case user input other than the given choices.



def wrong_answer(guesses):
    #this function will in picture if user input wrong answer in normal quiz or bonus level Quiz
    #it will decrese the value of guesses if user input is wrong
    #and if guesses == 0, it will take user to play_agian()
    guesses -= 1
    if guesses != 0:
        print("\nIncorrect Answer! Try Again.")
        print("Only " + str(guesses) + " guesses left.")
        return guesses
    else:
        print("\nGAME OVER!!! You have failed too many times.")
        play_again()


#Instruction about for game:
def quiz(string,answers):
    #this function will evaluate the answers for easy,medium and difficult level quiz mode.
    i = 1 #i will be used as index for answers and to indicate blank positions
    guesses = 5 #total number of guesses per blank
    print ("\nYou will get 5 guesses per problem.")
    while guesses != 0:
        print ("\nYour current paragraph reads as such:\n")
        print(string)
        user_answer = input("\nWhat should be substituted in for __" + str(i) + "__ ?").lower()
        if user_answer == answers[i-1]:
            print("\nCorrect Answer!")
            string = string.replace(("__" + str(i) +"__"),answers[i-1].upper())
            guesses = 5#if answer is correct gusses value will change to 5 in case if you have entered wrong answer before.
            i += 1
            if i == (len(answers) + 1):#(len(answers) + 1 )beacuse i will have +1 if all blanks are answered so we also have to increse len(answers)
                print (string)
                bonus_play()
                break
        else:
            guesses = wrong_answer(guesses)
            #it will deal with wrong inputs by taking input to wrong_answer

#bonus level game:
def bonus_quiz(string,answers,guesses):
    #this function will let the user play bonus level if clears pervious ground.
    #and it will evaluate the banus-mode's answers.
    i = 1 #i will be used as index for answers and to indicate blank positions
    while guesses != 0:
        print ("\nYour current paragraph reads as such:\n")
        print (string)
        user_answer = input("\nWhat should be substituted in for __" + str(i) + "__ ?")
        if user_answer == answers[i-1]:
            print("\nCorrect Answer!")
            string = string.replace(("__" + str(i) +"__"),answers[i-1].upper())
            guesses = 2#if answer is correct gusses value will change to 2 in case if you have entered wrong answer before.
            i += 1
            if i == (len(answers) + 1):
                print (string)
                print("\nCongratulations! You are a TRUE Avengers fan!")
                play_again()
                break
        else:
            guesses = wrong_answer(guesses)
            #it will deal with wrong inputs by taking input to wrong_answer


def gameplay():
    #ths fnction will display Welcome line and take the user to choices()
    print ("\nWelcome To Ultimate Avengers Quiz.")
    choices() #this function will choose the level of difficulty.


gameplay()
