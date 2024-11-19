import random

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
    print(computerNumber)
    while not weHaveAWinner:
        if turn > 0 or random.randint(1,2) == 1:
            userGuess = input("Guess my number: ")
            userGuess = list(userGuess)
            print(userGuess)
            if userGuess == computerNumber:
                weHaveAWinner = True
                print("Congratulations! You got it!")
            else:
                cows = 0
                bulls = 0
                for ug in range(0,4):
                    if computerNumber[ug] == userGuess[ug]:
                        bulls = bulls + 1
                    else:
                        if userGuess[ug] in computerNumber:
                            cows = cows + 1
                print(f"{bulls} bulls and {cows} cows")
        turn = turn + 1


    return False

while main():
    print("\n")    
