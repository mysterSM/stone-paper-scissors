from random import *
options = ["stone","paper","scissors"]
score = 0
comp_score=0
print("Welcome to the stone-paper-scissor game")
user_agreement_to_play = input("Enter 'start' to start the game and 'quit' to leave: ").lower().strip()
if user_agreement_to_play=='quit':
    print("Thanks for playing!")
elif user_agreement_to_play=='start':
    while True:
        user_choice = input("Choose: stone/paper/scissors (or 'quit' to leave): ").lower().strip()
        computer_choice=choice(options)
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        elif user_choice not in options:
            print("Invalid input, try again")
        elif user_choice==computer_choice:
            print(f"Your choice: {user_choice}")
            print(f"Computer's choice: {computer_choice}")
            print("Its a tie!")
            print("Updated score after dividing points: ")
            score+=0.5
            comp_score+=0.5
            print(f"Your score: {score}")
            print(f"Computer's score: {comp_score}")
        elif (user_choice=='stone' and computer_choice=='scissors') or (user_choice=='paper' and computer_choice=='stone') or (user_choice=='scissors' and computer_choice=='paper'):
            print(f"Your choice: {user_choice}")
            print(f"Computer's choice: {computer_choice}")
            print("You win!")
            score+=1
            print(f"Your score: {score}")
            print(f"Computer's score: {comp_score}")
        elif (user_choice=='stone' and computer_choice=='paper') or (user_choice=='paper' and computer_choice=='scissors') or (user_choice=='scissors' and computer_choice=='stone'):
            print(f"Your choice: {user_choice}")
            print(f"Computer's choice: {computer_choice}")
            print("Sorry, you lost!")
            comp_score+=1
            print(f"Your score: {score}")
            print(f"Computer's score: {comp_score}")
else:
    print("Invalid input, restart the game")
