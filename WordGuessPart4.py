import random

def GuessGame():
    f = open(r'C:\\Projects\\GuessGame\Words.txt', 'r')
    words = f.readlines()
    f.close
    history = []
    wordhistory = []
    Remaining = 7
    Wins = 0
    Losses = 0
    Stop = 0
    while Stop == 0:
        Winning = 0
        Losing = 0
        sAnswer = random.choice(words)
        repeat = 1
        while repeat == 1:
            if sAnswer in wordhistory:
                sAnswer = random.choice(words)
            else:
                repeat = 0
        Answer = sAnswer[:len(sAnswer)-1]
        wordhistory.append(sAnswer)
        Output = []
        for i in Answer:
            Output.append('_')
        while Winning == 0 and Losing == 0:
            guess = input(str(Output) + ' Please Guess a letter or the word: ').lower()
            if len(guess) > 1 and len(guess) < len(Answer):
                print("Error, word is longer than that, please guess again")
            elif len(guess) > len(Answer):
                print('Error, word is shorter than that, please guess again')
            else: 
                for i in history:
                    if i == guess:
                        print("Error, word or letter was already guessed, please try again.")
                if len(guess) >1:
                    if guess == Answer:
                        Wins = Wins + 1
                        Winning = 1
                        print('You got it! Number of spare guesses was  ' + str(Remaining) + ', answer was ' + Answer)
                    else:
                        Remaining = Remaining - 1
                        if Remaining == 0:
                            print('You are out of Guesses, you have lost, the answer was ' + Answer)
                            Losses = Losses + 1
                            Losing = 1
                        else:
                            z = guess in history
                            if z == False: 
                                history.append(guess)
                                print('Incorrect, you have ' + str(Remaining) + ' guesses left')
                            else:
                                Remaining = Remaining + 1 
                                print('Incorrect, you have ' + str(Remaining) + ' guesses left')
                else:
                    Count = 0
                    x = 0
                    while x < len(Answer):
                        if Answer[x] == guess:
                            Output[x] = guess
                            x = x + 1
                            Count = Count + 1
                        else:
                            x = x + 1
                    if Count == 0:
                        Remaining = Remaining - 1
                        if Remaining == 0:
                            print('You are out of Guesses, you have lost, the answer was ' + Answer)
                            Losses = Losses + 1
                            Losing = 1
                        else: 
                            a = guess in history
                            if a == False:
                                print('Incorrect, you have ' + str(Remaining) + ' guesses left')
                                history.append(guess)
                            else: 
                                Remaining = Remaining + 1
                                print('Incorrect, you have ' + str(Remaining) + ' guesses left')
                    else: 
                        b = guess in history
                        if b == False:
                            history.append(guess)
                            print('Correct! you currently have ' + str(Remaining) + ' guesses to left')
                        y = '_' in Output  
                        if y == False:
                            print('You win!')
                            Wins = Wins + 1
                            Winning = 1
        print('Wins = ' + str(Wins) + ' Losses = ' + str(Losses))
        valid_input = 0
        while valid_input == 0:
            Next = input('Would you like to play again? ').lower()  
            if Next == 'yes':
                print('Great! Here we go!')
                break 
            elif Next == 'no':
                print("Well played")
                valid_input == 1
                Stop = 1  
                break 
            else:
                print('Please type yes or no')
                Next = input('Would you like to play again?').lower()

GuessGame()