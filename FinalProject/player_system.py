"""
Author: Keyhan Khodabandehlou
Last updated: July 2026
Description:
Stores and manages FIFA World Cup player records using
a dictionary as a hash table.
"""

import csv

from player import Player


class PlayerSystem:
    """Manages all player records."""

    def __init__(self) -> None:
        # Key: player ID
        # Value: Player object
        self.players = {}

    def load_csv(self, file_name: str) -> None:
        """Loads player records from the CSV dataset."""

        try:
            with open(file_name, "r", encoding="utf-8-sig") as csv_file:
                reader = csv.DictReader(csv_file)

                for row in reader:
                    player = Player(
                        row["player_id"],
                        row["player_name"],
                        row["team"],
                        row["position"],
                        int(row["age"]),
                        int(row["goals"]),
                        int(row["assists"]),
                        float(row["tournament_rating"])
                    )

                    self.insert_player(player)

            print(f"{len(self.players)} players loaded.")

        except FileNotFoundError:
            print(f"Error: Could not find {file_name}.")

        except KeyError as error:
            print(f"Error: Column {error} was not found in the CSV.")
            print("Check the exact column names from check_columns.py.")

        except ValueError as error:
            print(f"Error converting data: {error}")

    def insert_player(self, player: Player) -> bool:
        """Adds a new player to the hash table."""

        if player.player_id in self.players:
            return False

        self.players[player.player_id] = player
        return True

    def search_player(self, player_id: str) -> Player | None:
        """Searches for a player using their ID."""

        return self.players.get(player_id)

    def delete_player(self, player_id: str) -> bool:
        """Deletes a player using their ID."""

        if player_id not in self.players:
            return False

        del self.players[player_id]
        return True

    def traverse_players(self) -> None:
        """Displays every player in the system."""

        if len(self.players) == 0:
            print("No players are stored.")
            return

        for player in self.players.values():
            print()
            print(player)
            print("-" * 35)
    
    def search_by_team(self, team: str) -> list:
        """Returns a list of players from the requested team."""

        matching_players = []

         # Traverse every player stored in the hash table
        for player in self.players.values():
            if player.team.lower() == team.lower():
              matching_players.append(player)

        return matching_players
    
    def search_by_position(self, position: str) -> list:
        """Returns a list of players who play the requested position."""

        matching_players = []

        # Traverse all players and check each position
        for player in self.players.values():
            if player.position.lower() == position.lower():
                matching_players.append(player)

        return matching_players
    
    def find_top_rated_player(self) -> Player | None: 
        """Returns the player with the highest rated tournament rating."""

        if len(self.players) == 0: 
            return None
        
        top_player = None
        
        for player in self.players.values():
            if top_player is None or player.player_rating > top_player.player_rating:
                top_player = player
        
        return top_player
    
    def get_top_players(self, amount: int = 10) -> list:
        """Returns the highest-rated players in descending order."""

        # Convert the hash table values into a list
        player_list = list(self.players.values())

        # Sort players from highest rating to lowest rating
        player_list.sort(
            key=lambda player: player.player_rating,
            reverse=True
        )

        return player_list[:amount]