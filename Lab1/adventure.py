"""
Name: Keyhan Khodabandehlou
Last updated: 17 June 2026
Description: Choose-Your-Adventure Game! for ENGR221 Lab 1 
"""

def adventure():
    """ This function runs one session of a choose your own adventure.
        Arguments: None
        Returns: None (Printed text is not returned)
    """

    print()

    print("Welcome, worthy adventurer, to The Swamp,")
    print("home to Ally the Golden Gator and sourdough bread!")

    print()

    #get player name and class
    player_name, player_class = create_player()

    print()
    
    #setting starting stats 
    if player_class == "Warrior":
        health = 100
        mana = 50
        print("A brave warrior, ready to confront any challenge.")
    elif player_class == "Mage":
        health = 50
        mana = 100
        print("A cunning mage, capable of outwitting the strongest foe.")
    
    print()

    print("Here are your beginning stats:")
    print("Health: {}".format(health))
    print("Mana: {}".format(mana))

    print()

    print(player_name, "your quest is to rescue Ally from the Spartans")
    print("who hold her captive.")
    print("Let us begin...")

    print()

    # First decision
    choice = input("Do you take the left path or right path? [left / right] ")

    if choice == "left":
        health = health - 20
        print("You chose the left path and lost 20 health.")
        print("Health: {}".format(health))

        choice2 = input("Do you fight or hide? [fight / hide] ")

        if choice2 == "fight":
            print("You fight the Spartan and rescue Ally. You win!")
        elif choice2 == "hide":
            print("You hide too long and Ally stays captured. You lose.")
        else:
            print("That was not a choice. You lose.")

    elif choice == "right":
        mana = mana - 20
        print("You chose the right path and used 20 mana.")
        print("Mana: {}".format(mana))

        choice2 = input("Do you run or sneak? [run / sneak] ")

        if choice2 == "sneak":
            print("You sneak past the Spartans and rescue Ally. You win!")
        elif choice2 == "run":
            print("You run away and fail the quest. You lose.")
        else:
            print("That was not a choice. You lose.")

    else:
        print("That was not a choice. You lose.")

    return 0


def create_player():
    """ Prompts the user for their name and class.
        Arguments: None
        Returns:
            - player_name (string): Name of the player
            - player_class (string): Class of the player
    """

    player_name = input("Before we begin, what should I call you? ")
    player_class = input("What is your specialty? [Warrior / Mage] ")

    while player_class != "Warrior" and player_class != "Mage":
        print("Please choose Warrior or Mage.")
        player_class = input("What is your specialty? [Warrior / Mage] ")

    return player_name, player_class


win = adventure()