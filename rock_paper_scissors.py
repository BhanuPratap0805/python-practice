import random

rock = "rock"
paper = "paper"
scissors = "scissors"

user_choice = input("What do you choose ? Type 0 for rock, type 1 for paper and type 2 for scissors: ")

if user_choice == "0":
    print(rock)
elif user_choice == "1":
    print(paper)
elif user_choice == "2":
    print(scissors)

choices = [rock,paper,scissors]
computer_choice = random.choice(choices)

print(computer_choice)

if user_choice == "0" and computer_choice == "scissors":
    print("You win")
elif user_choice == "0" and computer_choice == "rock":
    print("Draw")
elif user_choice == "0" and computer_choice == "paper":
    print("You lose")
elif user_choice == "1" and computer_choice == "scissors":
    print("You Lose")
elif user_choice == "1" and computer_choice == "rock":
    print("You Win")
elif user_choice == "1" and computer_choice == "paper":
    print("Draw")
elif user_choice == "2" and computer_choice == "scissors":
    print("Draw")
elif user_choice == "2" and computer_choice == "rock":
    print("You Lose")
elif user_choice == "2" and computer_choice == "paper":
    print("You Win")