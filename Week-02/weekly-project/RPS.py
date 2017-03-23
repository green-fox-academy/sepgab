#Game start
print('This is a Rock-paper-scissors game wrote in Python for lonely people.')
#változók: kör, pontok
import random

#Game initalization
winpts = int(input('Number of winning points: '))
score_user = 0
score_machine = 0
round_counter = 0

#game round
while max(score_user, score_machine) < winpts:
    machine_choice = random.randint(1,3)

    while True:
        user_input = input("Choose 'rock', 'paper' or 'scissors': ")
        if user_input == 'rock' or user_input == 'paper' or user_input == 'scissors':
            break

    if machine_choice == 1:
        print("The machine chose 'rock'.\n\n\n")
        if user_input == 'paper':
            score_user += 1
        elif user_input == 'scissors':
            score_machine += 1

    if machine_choice == 2:
        print("The machine chose 'paper'.\n\n\n")
        if user_input == 'rock':
            score_machine += 1
        elif user_input == 'scissors':
            score_user += 1

    if machine_choice == 3:
        print("The machine chose 'scissors'.\n\n\n")
        if user_input == 'rock':
            score_user += 1
        elif user_input == 'paper':
            score_machine += 1

    round_counter += 1
    #Display function
    print('Standings after round ' + str(round_counter))
    print('User score: ' + str(score_user))
    print('Machine score: ' + str(score_machine))

#Ending
if score_machine == winpts:
    print("\n Life is brutal - you lost!")
if score_user == winpts:
    print("\n Congrats, you won!!!")
