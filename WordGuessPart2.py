Guesses = []
Answer = "pasta"
Remaining = 7
Output = '_____'

def GuessGame():
    guess = input(Output + 'Please Guess a letter or the word:')
    if len(guess) > 1 and len(guess) < len(Answer):
        print("Error, word is longer than that, please guess again")
        GuessGame()
    elif len(guess) > len(Answer):
        print('Error, word is longer than that, please guess again')
        GuessGame()
    else:
        print('success')


GuessGame()