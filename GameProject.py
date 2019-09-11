import random

# Get the guess from the user.


def getGuess():
    return list(input("What is your guess?: "))

# using the number generate code by computer randomly, and slice up the
# list for only generating 3 digits code.


def generateCode():
    digits = [str(num) for num in range(10)]

    # Use random function for inputted data.

    random.shuffle(digits)

    # Return the first 3 elements from the list

    return digits[:3]


# function for clue generation.


def generateClue(code, userGuess):
    # if the guess is correct, return a termination string in main function.
    if userGuess == code:
        return 'CODEISCRACKED'
    # create a list for appending the clues. These clues will be used to speculate the number.
    clues = []
    ind = 0
    for ind, num in enumerate(userGuess):  # Enumerate function to fetch out index and elements.
       # eg:
        # index    |      values
        #  0       |      num[0]
        #  1       |      num[1]
        #  2       |      num[2]
        if num == code[ind]:
            clues.append('Match')

        elif num in code:
            clues.append('Close...')

    if not clues:
        return['Nope']
    else:
        return clues

def main():
    print("WELCOME CODE BREAKER! Let's play.", end='\n')
    secretCode = generateCode() # generate code randomly by calling random fn.
    clueReport = [] # create an empty list, to terminate the following controlFlow (loop).
    while clueReport != 'CODEISCRACKED':
        guess = getGuess()
        clueReport = generateClue(guess, secretCode)
        print("YOUR GUESS RESULT: ")
        for i in clueReport:
            print(i)


if __name__ == "__main__":
    main()


