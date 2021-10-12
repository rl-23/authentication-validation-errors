from random import randint
#imports random number Module

number_to_guess = randint(1,101)
#random number is generated between 1-100

number_guessed = False
#number has not been guessed yet, so is set as false(it needs to be guesse correctly)

while number_guessed == False:
#while loop so the user can continuously guess the number
    try:
        guess = int(input("Enter a number between 1 and 100\n> "))
    #input for the user to guess number

        if guess > number_to_guess and guess <= 100 and guess > 0:
            print("Too high! Try again ...")
            #tells user if the inputted number is higher
        elif guess < number_to_guess and guess <= 100 and guess > 0 :
            print("Too low! Try again...")
            #tells user if the inputted number is lower
        elif guess > 100 or guess < 0:
            print("Invalid! Try again...")
            #detects if number is higher/lower than 100, and therefore invalid

        else:
            print("You got it!")
            number_guessed = True
            #number is correct
    except ValueError:
        print("Value not acceptable.")
    except TypeError:
        print("Value not acceptable.")
    except KeyboardInterrupt:
        print("Please don't use keyboard shortcuts.")
    except RuntimeError:
        print("You broke the code.")

#try and except setup for all the errors possible
