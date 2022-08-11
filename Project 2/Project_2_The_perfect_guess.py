
import random
randomNumber = random.randint(1,100)
# print(randomNumber)

userGuess = None
guesses = 0

while (userGuess != randomNumber):
    userGuess = int(input('Enter your guess:\n'))
    guesses = guesses + 1 

    if (userGuess==randomNumber):
        print('You guessed it right!')
    else:
        if (userGuess > randomNumber):
            print('Your guess is wrong! Please enter a smaller number.') 
        else:
            print('Your guess is wrong! Please enter a larger number.') 
    print('----------')           

print(f'You guessed it right in {guesses} guesses.')       


with open('highscore.txt','r') as f :
    highscore = int(f.read()  )   

with open('highscore.txt','w') as f:
    if guesses < highscore:
        print('You just broke the highscore!')
        f.write(str(guesses))       
