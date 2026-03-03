secretWord = "THE LONG SHOE"
blankWord = ["_"] * len(secretWord)
positions = []
guessedLetters = [" ", ""]
lives = 10
firstPass = False

while True:
    if firstPass == True:
        print("Current letters found in word:", "".join(blankWord))
        print("Current letters guessed:", guessedLetters[2:])
        guess = input("Enter a letter to guess: ").upper()
        if guess != "":
            guess = guess[0]
        if guess in guessedLetters:
            print("Letter already guessed")
            guess = " "
        else:
            guessedLetters.append(guess)
    else:
        firstPass = True
        guess = " "

    foundLetter = False
    for i in range(len(secretWord)):
        if secretWord[i] == guess:
            positions.append(i)
            foundLetter = True
    
    if(foundLetter == True):
        for pos in positions:
            blankWord[pos] = secretWord[pos]
        foundLetter = False
    else:
        lives -= 1
        print("You didn\'t find a letter")
        print("Lives left:", lives)

    if(secretWord == "".join(blankWord)):
       print("You guessed the word")
       print(secretWord)
       break

    if(lives == 0):
        print("You lost")
        print("The word was:", secretWord)
        break