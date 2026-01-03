print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
cross_road = input('''You're at a cross road.Where do you wanna go ?  Type "Left" or "Right": ''').lower()

if cross_road == "left":
    wait_or_swim = input("You come to a lake.There is an island in the middle of the lake.Type 'wait' to wait for a boat.Type 'swim' to swim across.: ").lower()

    if wait_or_swim == "wait":
        doors = input("There are 3 doors infront of you. 'Red'  'Blue'  'Green': ").lower()
        
        if doors == "red":
            print('''There is fire behind that door You die.Game over''')

        elif doors == "blue":
            print("There is endless ocean.You lose")

        elif doors == "green":
            print("Your reached the island.Congratulations You reached the island.")
    elif wait_or_swim == "swim":
        print("Sharks ate you when you were trying to swim.Game over")
elif cross_road == "right":
    print("There's nothing out there.Restart.")