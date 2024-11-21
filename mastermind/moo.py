import random

def countBullsAndCows(guess, actual):
    cows = 0
    bulls = 0
    for ug in range(0,4):
        if actual[ug] == guess[ug]:
            bulls = bulls + 1
        else:
            if guess[ug] in actual:
                cows = cows + 1
    return bulls, cows

def main():
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(numbers)
    computerNumber = numbers[0:4]
    userNumberIsValid = False
    while not userNumberIsValid:
        userNumber = input("Please enter a 4 digit number. Each digit must be unique.\n")
        try:
            test1 = int(userNumber)
            if test1 < 123 or test1 > 9876:
                continue
        except:
            continue
        test2 = list(userNumber)
        if len(test2) != 4 or len(set(test2)) != len(test2):
            continue
        userNumber = test2
        userNumberIsValid = True
    weHaveAWinner = False
    turn = 0
    computerGuessSequence = numbers.copy()
    random.shuffle(computerGuessSequence)
    computerGuessList = []
    knownNumbers = [-1, -1, -1, -1]
    while not weHaveAWinner:
        if turn > 0 or random.randint(1,2) == 1:
            userGuess = input("Guess my number: ")
            userGuess = list(userGuess)
            if userGuess == computerNumber:
                weHaveAWinner = True
                print("Congratulations! You got it!")
                continue
            else:
                bulls, cows = countBullsAndCows(userGuess, computerNumber)
                print(f"{bulls} bulls and {cows} cows")
        if turn == 0:
            newGuess = computerGuessSequence[0:4]
        else:
            shuffledNumbers = numbers.copy()
            random.shuffle(shuffledNumbers)
            newGuess = knownNumbers.copy()
            random.shuffle(newGuess)
            if -1 in newGuess:
                for i in range(0,4):
                    if newGuess[i] == -1:
                        newGuess[i] = shuffledNumbers[i]

        bulls, cows = countBullsAndCows(newGuess, userNumber)
        if bulls == 4:
            weHaveAWinner = True
            print("Ha! I win!")
            continue
        computerGuessList.append(newGuess + [bulls, cows])
        if bulls + cows == 0:
            for i in range(0,4):
                numbers.remove(newGuess[i])
        if bulls + cows == 4:
            knownNumbers = newGuess.copy()
        newGuess = ''.join(newGuess)
        print(f"My guess: {newGuess}")
        print(f"{bulls} bulls and {cows} cows")

        turn = turn + 1

    newGame = input("Would you like to play again (Y/N)? ")
    return newGame.lower() == 'y'

while main():
    print("\n")    
