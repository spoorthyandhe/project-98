import random 

print(" Number guessing game :")

number = random.randint(1,9)
chances = 0

print ("Guess a number (between 1 and 9): ")
# while loop to count the umbers of changes
while chances <5:
    guess = int(input("Enter your guess: "))

#compare the user enteres number with the number 

    if guess == number:
    #if number entered by user is same as the generated
    #number by randint function then break from loop using loop
    #control statement "break"
        print(" Congatulation YOU WON!!!")
        break

    elif guess < number:
        print("your guess was too low: guess a number higher than ",guess)

    else:
        print("your guess was too high: guess a number lower than ",guess)

chances = chances+1

#check whether the user gussed the correct number
if not chances <5 :
    print("YOU LOSE!!! The number is",number)
