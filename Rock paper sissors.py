print("Welcome the Rock Paper Scissors Game")
print("Rules of the game are as follows:")
print("1.Rock beats scissors")
print("2.Scissors beats paper")
print("3.Paper beats rock")

choices = ["rock","paper","scissors"]
user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
import random
computer_choice = random.choice(choices)

if user_choice == computer_choice:
    print("It is a tie! Both chose", user_choice)
elif (user_choice =="rock" and computer_choice =="scissors")or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
    print("You win! You chose", user_choice, "and the computer chose", computer_choice)
else:
    print("You lose! You chose", user_choice, "and the computer chose", computer_choice)


print("Thanks for playing the game!")