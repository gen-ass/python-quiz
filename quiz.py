#A - When a answer is correct it is substututed into the text in list format
containers = ['-1-','-2-','-3-','-4-']

#B - Questions appearing during promt in list format
questions = ["\n Replace with.. -1- :",
            "\n Replace with.. -2- :",
            "\n Replace with.. -3- :",
            "\n Replace with.. -4- :"]


#C - Easy, Medium and Hard text templates in dictionary format
game_text = {'level1':"\n'Level1' difficulty: \n\n The -1- is a vast subdivision of -2-, composed of many -3- endeavors and disciplines. It is a broader term than \"art\", which, as a description of a field, usually means only the -4- arts. HINT first line - https://en.wikipedia.org/wiki/Portal:Arts\n",
'level2':"\n'Level2' difficulty: \n\n Ancient -1- art saw the veneration of the -2- form and the development of equivalent -3- to show musculature, poise, -4- and anatomically correct proportions. HINT second line first paragraph - https://en.wikipedia.org/wiki/Portal:Arts\n",
'level3':"\n'Level3' difficulty: \n\n Paradoxically the -1- of new technologies were greatly -2- by the -3- tribal arts of Africa and -4- HINT last line second paragraph - https://en.wikipedia.org/wiki/Portal:Arts\n"}


#D - Answers in dictionary format
answers = {'level1':['arts','culture','creative','visual'],'level2':['Greek','animal','skills','beauty'],'level3':['expressions','influenced','ancient','Oceania']}

#E - Easy, Medium and Hard options can be input by keeping the option list empty so any value can be entered
options = []

#F ------------------- Defining the variables and methods that wil be used in the game -------------
def game():
    #1 - Introduction section

    # Input - Users are asked to enter difficulty by prompting the options level.
    # Output - User is given a response of what his option was, if the response is invalid user is prompted to enter valid one.
    user_input = "Note: ANSWERS are CaSe SeNsitive\nPlease select a game difficulty by typing it in!\nPossible options:  level1  level2  level3 \nPlease type your game difficulty:"
    difficulty = raw_input(user_input)
    instructions = "\nYour selection was '" + str(difficulty) + "'."
    print instructions
    if difficulty.lower() == 'level3' or difficulty.lower() == 'level2' or difficulty.lower() == 'level1':
        return start(difficulty)
    else:
        incorrect_difficulty = "\n '" + difficulty + "' Is not valid. Make a valid selection\n"
        print incorrect_difficulty
        return game()

def option(difficulty,option_index,guesses):
    #2 - Here a player inputs his answer: level1, level2, level3

    # Input - When user inputs difficulty in def game() the def option() is called. 
    # Output - The level of difficulty is then passed back to the user prompt. If he selects an invalid statement then the user is prompted to select a valid option again.
    print game_text[difficulty]
    if option_index == len(answers[difficulty]):
        return win(guesses)
    options.append(raw_input(questions[option_index]))
    if options[option_index] == answers[difficulty][option_index]:
        return correct(option_index,difficulty,guesses)
    else:
        return incorrect(guesses,difficulty,option_index)

def start(difficulty):
    #3 - The player gets the option of selecting how many chioces he gets before losing.

    # Input - User is prompted to select how many times guesses can be made
    # Output - The guesses are then displayed to the user of how many times incorrect options can be made before it is game over
    guesses_prompt = "Please select the number of guesses you'd like:"
    guesses = raw_input(guesses_prompt)
    if int(guesses):
        guesses = int(guesses)
        guess_text = "\nYou will get " + str(guesses) + " chances."
        print guess_text
        return option(difficulty.lower(),0,guesses)

def win(guesses):
    #4 - When a payer wins the game

    # Input - Correct guesses are counted
    # Output - Guesses are then returned as a prompt on the screen indicating the player has won and with how many guesses remains.
    winning = "You've won and : " + str(guesses) + " option(s) remain(s)\nVisit the victory video(not spam or malicious, just some silliness): https://youtu.be/1npWhzBJAzA\n"
    return winning

def correct(option_index,difficulty,guesses):
    #5 - When the correct answer is made

    # Input - The user inputs an answer if correct this will run
    # Output - User gets a screen prompt that a correct answer has been made
    correct_answer = "\nCorrect! '" + str(options[option_index]) + "' is the correct answer!"
    print correct_answer
    game_text[difficulty] = game_text[difficulty].replace(containers[option_index],options[option_index])
    return option(difficulty,option_index+1,guesses)

def incorrect(guesses,difficulty,option_index):
    #6 - What will happen if the player has made incorrect options

    # Input - The user inputs an answer if incorrect this will run
    # Output - User gets a screen prompt that an incorrect answer has been made and a prompt tells user how many guess attempts remain. If the attempts are exceeded then a prompt is given that the game is over
    incorrect_option = options.pop()
    min_guesses = 0
    if guesses == min_guesses:
        game_over = "You've guessed incorrectly too many times\nTry again!"
        return game_over
    else:
        guesses -= 1
        incorrect_answer_text = "\n'" + incorrect_option + "' unfortunately that is incorrect!\nTry again, guesses remaining : " + str(guesses) 
        print incorrect_answer_text
        return option(difficulty,option_index,guesses)

#7. Run game program
print game()
