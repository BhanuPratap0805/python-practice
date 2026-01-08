import random

word_list = ["dog", "cat", "horse", "cow", "sheep",
    "goat", "pig", "rabbit", "deer", "camel",
    "lion", "tiger", "leopard", "cheetah", "panther",
    "elephant", "giraffe", "zebra", "hippopotamus", "rhinoceros",
    "monkey", "gorilla", "chimpanzee", "orangutan", "baboon",
    "wolf", "fox", "bear", "hyena", "jackal",
    "kangaroo", "koala", "platypus", "wombat", "wallaby",
    "penguin", "ostrich", "eagle", "falcon", "vulture",
    "snake", "lizard", "crocodile", "alligator", "tortoise",
    "frog", "toad", "salamander", "newt", "axolotl",
    "whale", "dolphin", "shark", "octopus", "seal",]

chosen_word = random.choice(word_list)

placeholder = ""

for letter in chosen_word:
    print("_", end="")

game_over = False
correct_letters = []

lives = 6

while not game_over:
    guess = input("\nGuess a letter: ").lower()

    display= ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"  

    print(display)

    if "_" not in display:
        game_over = True
        print("You win.")

    if guess not in chosen_word:
        lives -= 1
        print("Lives Remaining: ",lives)
        if lives == 0:
            game_over = True
            print("You lose.")
            print("The word was: ",chosen_word)