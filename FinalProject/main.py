"""
Author: Keyhan Khodabandehlou
Last updated: July 30 2026
Description:
Runs the FIFA World Cup Player Performance System and
allows the user to search, add, delete, and display players.
"""

from player import Player
from player_system import PlayerSystem


# Name of the dataset file
DATA_FILE = "fifa_world_cup_2026_player_performance.csv"


def display_menu() -> None:
    """Displays the program options."""

    print()
    print("FIFA World Cup Player Performance System")
    print("----------------------------------------")
    print("1. Search for a player by ID")
    print("2. Add a player")
    print("3. Delete a player")
    print("4. Display all players")
    print("5. Search for players by team")
    print("6. Search for players by position")
    print("7. Display top-rated player")
    print("8. Display top 10 players")
    print("9. Exit")


def add_player(system: PlayerSystem) -> None:
    """Gets player information from the user and adds a new player."""

    print()
    print("Add a New Player")
    print("----------------")

    # Get identifying information from the user
    player_id = input("Player ID: ").strip()
    player_name = input("Player name: ").strip()
    team = input("National team: ").strip()
    position = input("Position: ").strip()

    try:
        # Convert numerical input into the correct data types
        age = int(input("Age: "))
        goals = int(input("Goals: "))
        assists = int(input("Assists: "))
        player_rating = float(input("Player rating: "))

    except ValueError:
        # Stops the operation if user enters invalid numerical data
        print("Age, goals, assists, and rating must be numbers.")
        return

    # Create a Player object with the entered information
    player = Player(
        player_id,
        player_name,
        team,
        position,
        age,
        goals,
        assists,
        player_rating
    )

    # Insert the player only if the ID is not already in the hash table
    if system.insert_player(player):
        print(f"{player_name} was added successfully.")
    else:
        print(f"A player with ID {player_id} already exists.")


def run_program() -> None:
    """Loads the dataset and runs the main menu."""

    # Create the player management system
    system = PlayerSystem()

    # Load all player records from the CSV file
    system.load_csv(DATA_FILE)

    # Controls whether the menu loop should continue running
    running = True

    while running:
        display_menu()
        
        # Read the user's menu selection
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            # Use the player ID as a hash-table key
            player_id = input("Enter the player ID: ").strip()
            player = system.search_player(player_id)

            # search_player returns NONE when key does not exist
            if player is None:
                print("Player not found.")
            else:
                print()
                print(player)

        elif choice == "2":
            # Call a seperate player using their unique ID
            add_player(system)

        elif choice == "3":
            # Delete a player using their unique ID
            player_id = input("Enter the player ID to delete: ").strip()

            if system.delete_player(player_id):
                print("Player deleted successfully.")
            else:
                print("Player not found.")

        elif choice == "4":
            # Traverse the hash table and display every stored player
            system.traverse_players()

        elif choice == "5":
            # Search for all players belonging to a national team
            team = input("Enter the national team: ").strip()
            matching_players = system.search_by_team(team)

            if len(matching_players) == 0:
                print(f"No players were found for {team}.")
            else:
                print(f"\nPlayers from {team}:")

                for player in matching_players:
                    print()
                    print(player)
                    print("-" * 35)

        elif choice == "6":
            # Ask the user which playing position to search for
            position = input(
                "Enter a position "
                "(Goalkeeper, Defender, Midfielder, or Forward): "
            ).strip()

            matching_players = system.search_by_position(position)

            if len(matching_players) == 0:
                print(f"No players were found at the {position} position.")
            else:
                print(f"\nPlayers at the {position} position:")

                # Display every player whose position matches
                for player in matching_players:
                    print()
                    print(player)
                    print("-" * 35)

        elif choice == "7":
            # Traverse all players to find the highest rating
            top_player = system.find_top_rated_player()

            if top_player is None:
                print("No players are stored.")
            else:
                print("\nTop-Rated Player")
                print("----------------")
                print(top_player)

        elif choice == "8":
            # Get a list contiaining the ten highest-rated players
            top_players = system.get_top_players(10)

            if len(top_players) == 0:
                print("No players are stored.")
            else:
                print("\nTop 10 Players")
                print("--------------")

                # Start the leaderboard ranking at first place
                rank = 1

                for player in top_players:
                    print(
                        f"{rank}. {player.player_name} "
                        f"({player.team}) - "
                        f"{player.player_rating}"
                    )
                    rank += 1
        
        elif choice == "9":
            # End the menu loop and close the program
            running = False
            print("Program closed.")

        else:
            # Handle menu entries outside valid loop
            print("Please enter a number from 1 through 9.")

# Run program only when main.py is executed directly
if __name__ == "__main__":
    run_program()