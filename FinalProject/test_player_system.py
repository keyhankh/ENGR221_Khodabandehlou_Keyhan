"""
Author: Keyhan Khodabandehlou
Last updated: July 30, 2026
Description:
Tests the main operations of the PlayerSystem class.
"""

from player import Player
from player_system import PlayerSystem


def run_tests() -> None:
    """Tests insertion, searching, deletion, and traversal."""

    system = PlayerSystem()

    # Create sample players for testing
    player_one = Player(
        "TEST001",
        "Test Player One",
        "United States",
        "Forward",
        24,
        3,
        2,
        8.5
    )

    player_two = Player(
        "TEST002",
        "Test Player Two",
        "Spain",
        "Midfielder",
        27,
        1,
        4,
        7.9
    )

    # Test insertion
    print("Testing insertion:")
    print(system.insert_player(player_one))
    print(system.insert_player(player_two))

    # A duplicate ID should not be inserted
    print("Testing duplicate insertion:")
    print(system.insert_player(player_one))

    # Test searching
    print("\nTesting search:")
    found_player = system.search_player("TEST001")
    print(found_player)

    # Test searching for an ID that does not exist
    print("\nTesting unsuccessful search:")
    print(system.search_player("DOES_NOT_EXIST"))

    # Test searching by team
    print("\nTesting team search:")
    team_players = system.search_by_team("Spain")

    for player in team_players:
        print(player)

    # Test searching by position
    print("\nTesting position search:")
    position_players = system.search_by_position("Forward")

    for player in position_players:
        print(player)

    # Test top-rated player
    print("\nTesting top-rated player:")
    print(system.find_top_rated_player())

    # Test deletion
    print("\nTesting deletion:")
    print(system.delete_player("TEST001"))

    # Confirm that the player was deleted
    print("\nSearching after deletion:")
    print(system.search_player("TEST001"))


if __name__ == "__main__":
    run_tests()