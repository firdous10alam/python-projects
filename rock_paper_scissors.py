# Here I learned how to use lists in loop .lower funtion.

import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:

    user_input = input("Enter rock/paper/scissors or Q to quit: ").lower()

    if user_input == 'q':
        break

    elif user_input not in options:
        continue

    random_number = random.randint(0,2)
    # 0 : rock, 1 : paper, 2 : scisssors
    computer_guess = options[random_number]

    if user_input == "rock" and computer_guess == "scissors":
        print("You won!")
        user_wins += 1
    
    elif user_input == "scissors" and computer_guess == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_guess == "rock":
        print("You won!")
        user_wins += 1

    else:
        print("Computer won!")
        computer_wins += 1

print(f'You won {user_wins} times and Computer won {computer_wins} times.')

