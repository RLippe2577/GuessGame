

def GuessGame():
    history = []
    Remaining = 7
    Answer = "pasta"
    Output = ['_','_','_','_','_',]
    Winning = 0
    Losing = 0
    while Winning == 0 and Losing == 0:
        #print(history)
        guess = input(str(Output) + ' Please Guess a letter or the word:').lower()
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
                    Winning = 1
                    print('You got it! Number of spare guesses was  ' + str(Remaining) + ', answer was ' + Answer)
                else:
                    Remaining = Remaining - 1
                    if Remaining == 0:
                        print('You are out of Guesses, you have lost')
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
                        print('You are out of Guesses, you have lost')
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
                        Winning = 1


GuessGame()