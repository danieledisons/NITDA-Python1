from random import randint
def numberGuess():
    attempts = 0
    level = int(input("Choose your level: \n For Easy type 1 \n For Intermediate type 2 \n For Hard type 3 \n"))


    if level == 1:
        attempts = 10
        value = randint(0, 100)

        while True: 
            response = int(input("Guess what random number the computer picked: "))
            if response == value:
                print(f"You guessed right!! The correct number is {value}")
                break

            if response != value:
                attempts = attempts - 1
                print(f"You guessed wrong. Try again")
                print(f"You have {attempts} attempts")
            
            if attempts == 0:
                print(f"Sorry, you have run out attempts, the hidden number is {value}")
                break

    if level == 2:
        attempts = 7
        value = randint(0, 500)

        while True: 
            response = int(input("Guess what random number the computer picked: "))
            if response == value:
                print(f"You guessed right!! The correct number is {value}")
                break

            if response != value:
                attempts = attempts - 1
                print(f"You guessed wrong. Try again")
                print(f"You have {attempts} attempts")
            
            if attempts == 0:
                print(f"Sorry, you have run out attempts, the hidden number is {value}")
                break
    
    if level == 3:
        attempts = 5
        value = randint(0, 1000)

        while True: 
            response = int(input("Guess what random number the computer picked: "))
            if response == value:
                print(f"You guessed right!! The correct number is {value}")
                break

            if response != value:
                attempts = attempts - 1
                print(f"You guessed wrong. Try again")
                print(f"You have {attempts} attempts")
            
            if attempts == 0:
                print(f"Sorry, you have run out attempts, the hidden number is {value}")
                break

numberGuess()