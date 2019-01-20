import random # importing the python random module

computer_guess = random.randrange(1, 100) # Generates random numbers from 1 to 99

count = 0 # Counts the number of times the user played

count_score = 0 # Counts the user's score

number_of_trials = 5 # Number of times the user can play

# while the number of times the user tried is less that the specified maximum number of times

while count < number_of_trials:

    user_guess = int(input("Enter your guess: "))  # Prompts the user to enter a number

    if computer_guess == user_guess:

        print("You got that right")
        count_score += 1

    elif computer_guess > user_guess:

        print("Your guess was too low. Try again")
        
    else:
        print("Your guess was too high. Try again")

    count += 1

print("You got ", count_score, "out of a total of ",number_of_trials, "trials")
